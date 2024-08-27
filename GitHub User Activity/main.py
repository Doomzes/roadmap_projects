import argparse
import requests

class UserActivity:
    def __init__(self):
        self.transactions = []

    def event(self) -> None:
        header = f"{'ID':<4} {'Name events':<52} {'Date':<20}"
        print(header)
        print("-" * len(header))
        for i in json:
            if i['type'] == 'PushEvent':
                self.transactions.append({"ID": f"{len(self.transactions) + 1}", "Name events": f"Pushed {i['payload']['size']} commits to {i['repo']['name']}",
                                          "Date": f"{str(i['created_at'])[:10]} {str(i['created_at'])[11:19]}"})
            elif i['type'] == 'IssuesEvent':
                self.transactions.append({"ID": f"{len(self.transactions) + 1}", "Name events": f"{str(i['payload']['action']).capitalize()} a new issue in {i['repo']['name']}",
                     "Date": f"{str(i['created_at'])[:10]} {str(i['created_at'])[11:19]}"})
            elif i['type'] == 'WatchEvent':
                self.transactions.append(
                    {"ID": f"{len(self.transactions) + 1}", "Name events": f"Starred {i['repo']['name']}",
                     "Date": f"{str(i['created_at'])[:10]} {str(i['created_at'])[11:19]}"})

        for transaction in self.transactions:
            print(f"{transaction['ID']:<4} {transaction['Name events']:<52} {transaction['Date']:<12}")


user_event = UserActivity()

parser = argparse.ArgumentParser(description="Task management system")
parser.add_argument('name_user', help='Name user')

args = parser.parse_args()

res = requests.get(f'https://api.github.com/users/{args.name_user}/events')

json = res.json()

if res.status_code == 200:
    user_event.event()
elif res.status_code == 404:
    print("User if not found")