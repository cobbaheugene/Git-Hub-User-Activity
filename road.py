"""
This script fetches the latest events for a given GitHub username and prints them.
"""

import requests
import sys
from rich import print

def get_latest_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        event = response.json()
        latest_events = event[:3]
        print(f"Latest events for [bold green]{username}[/bold green]:")
        for event in latest_events:
            if event['type'] == 'IssueCommentEvent':
                print(f"- :smiley: commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'PushEvent':
                print(f"- :smiley: pushed to {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"- :smiley: created issue {event['payload']['issue']['number']}")
            elif event['type'] == 'WatchEvent':
                print(f"- :smiley: starred {event['repo']['name']}")
    else:
        print(f"Error fetching events for {username}: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_latest_events(sys.argv[1])
    else:
        print("Please provide a GitHub username as a command line argument.")