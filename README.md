# JiraTime

A command-line tool to manually track time entries and manage local logs.

## Installation

No external dependencies required beyond Python 3.11.

## Usage

1. List logs: `python main.py logs`
2. Create entry: `python main.py add --issue TEST-1 --minutes 60`
3. Sync to Jira (mocked): `python main.py sync`

## Configuration

None. Uses local file storage.