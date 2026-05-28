# JiraTime CLI

## What it does
A command-line tool to track work time and sync with Jira API locally.

## Installation

No dependencies required for installation. Just ensure you have Python 3.11+.

## Usage

Add a time entry:
```bash
python main.py add --project TEST --hours 1.5
```

Sync to Jira:
```bash
python main.py sync --token $JIRA_TOKEN
```

Export logs:
```bash
python main.py export --format csv
```

## Configuration

Requires a `JIRA_TOKEN` environment variable for API authentication.
