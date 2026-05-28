import pytest
import os
import json
from unittest.mock import patch, MagicMock
import responses

# Mocking Jira API
@responses.activate
def test_jira_api_sync():
    # Mock the Jira API endpoint
    responses.add(
        responses.POST,
        "https://my-jira-instance.atlassian.net/rest/api/3/issue",
        json={"id": "10010", "key": "TEST-1"},
        status=200
    )
    
    # Call the sync function
    # Assuming a function sync_to_jira(token) exists
    # We verify the mock was hit
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "https://my-jira-instance.atlassian.net/rest/api/3/issue"

def test_local_persistence():
    # Mock file write
    test_data = {"project": "TEST", "hours": 1.0}
    with patch('builtins.open', mock_open(create=True)) as mock_file:
        with patch('json.dump') as mock_dump:
            # Logic to write file
            with open('time_logs.json', 'w') as f:
                json.dump(test_data, f)
    assert mock_file.called
    # Cleanup
    if os.path.exists('time_logs.json'):
        os.remove('time_logs.json')

def test_csv_export():
    # Mock file write
    with patch('builtins.open', mock_open(create=True)) as mock_file:
        # Logic to write CSV
        with open('export.csv', 'w') as f:
            f.write("project,hours,date\n")
    assert mock_file.called
    # Cleanup
    if os.path.exists('export.csv'):
        os.remove('export.csv')

if __name__ == "__main__":
    pytest.main(["-v"])
