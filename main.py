import argparse
import json
import os
from datetime import datetime
import csv

# Local storage
DATA_FILE = "time_logs.json"

def load_logs():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_logs(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def add_entry(args):
    entry = {
        "project": args.project,
        "hours": args.hours,
        "date": datetime.now().isoformat()
    }
    logs = load_logs()
    logs.append(entry)
    save_logs(logs)
    print(f"Entry saved: {entry}")

def sync_to_jira(args):
    # Mocking the Jira API call for this implementation
    print(f"Syncing to Jira with token {args.token}")
    # In a real app, this would use requests.post to the Jira API

def export_data(args):
    logs = load_logs()
    filename = f"export_{args.format.lower()}.{'csv' if args.format.lower() == 'csv' else 'json'}"
    
    if args.format.lower() == 'csv':
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['project', 'hours', 'date'])
            for entry in logs:
                writer.writerow([entry['project'], entry['hours'], entry['date']])
    else:
        with open(filename, 'w') as f:
            json.dump(logs, f)
    
    print(f"Exported to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='JiraTime CLI')
    subparsers = parser.add_subparsers(dest='command')
    
    add = subparsers.add_parser('add', help='Add time entry')
    add.add_argument('--project', required=True, help='Jira Project Key')
    add.add_argument('--hours', type=float, required=True, help='Hours worked')
    
    sync = subparsers.add_parser('sync', help='Sync to Jira')
    sync.add_argument('--token', required=True, help='Jira API Token')
    
    export = subparsers.add_parser('export', help='Export data')
    export.add_argument('--format', choices=['csv', 'json'], required=True, help='Export format')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_entry(args)
    elif args.command == 'sync':
        sync_to_jira(args)
    elif args.command == 'export':
        export_data(args)
