import json
import os
from datetime import datetime

def create_entry(issue_key, minutes):
    entry = {
        "issue": issue_key,
        "duration_minutes": minutes,
        "timestamp": datetime.now().isoformat(),
        "status": "pending"
    }
    logs = []
    if os.path.exists('logs.json'):
        with open('logs.json', 'r') as f:
            logs = json.load(f)
    logs.append(entry)
    with open('logs.json', 'w') as f:
        json.dump(logs, f, indent=2)
    return entry

def get_logs():
    if not os.path.exists('logs.json'):
        return []
    with open('logs.json', 'r') as f:
        return json.load(f)

# This is a placeholder to make the import work
# The actual logic will be in the functions
import sys
sys.path.insert(0, '/workspace/projects/JiraTime')

# Mocking the API call for the test runner
# In a real app, we would import requests here
print("JiraTime initialized. Ready for manual entry.")