import argparse
import requests

class UserActivity:
    def __init__(self):
        self.transactions = []

    def wrap_text(self, text, width) -> None:
        #Разбивает текст на строки длиной не более width символов.
        return [text[i:i + width] for i in range(0, len(text), width)]

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
            description_lines = self.wrap_text(transaction['Name events'], 52)
            print(f"{transaction['ID']:<4} {description_lines[0]:<52} {transaction['Date']:<12}")

            for line in description_lines[1:]:
                print(f"{'':<4} {line:<52}")



user_event = UserActivity()

parser = argparse.ArgumentParser(description="Task management system")
parser.add_argument('name_user', help='Name user')

args = parser.parse_args()

res = requests.get(f'https://api.github.com/users/{args.name_user}/events')

json = res.json()

if res.status_code == 200:
    user_event.event()
elif res.status_code == 404:
    print("User is not found")