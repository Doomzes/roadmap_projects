import argparse
import requests

class UserActivity:
    def __init__(self):
        pass

    def event(self) -> None:
        for i in json:
            if i['type'] == 'PushEvent':
                print(f"- Pushed {i['payload']['size']} commits to {i['repo']['name']} at {str(i['created_at'])[:10]} {str(i['created_at'])[11:19]}")
            elif i['type'] == 'IssuesEvent':
                print(f"- {str(i['payload']['action']).capitalize()} a new issue in {i['repo']['name']} at {str(i['created_at'])[:10]} {str(i['created_at'])[11:19]}")
            elif i['type'] == 'WatchEvent':
                print(f"- Starred {i['repo']['name']} at {str(i['created_at'])[:10]} {str(i['created_at'])[11:19]}")


user_event = UserActivity()

parser = argparse.ArgumentParser(description="Task management system")
parser.add_argument('name_user', help='Name user')

args = parser.parse_args()

res = requests.get(f'https://api.github.com/users/{args.name_user}/events')

json = res.json()

if res.status_code == 200:
    print("User is found")
    user_event.event()
elif res.status_code == 404:
    print("User if not found")