import argparse
import requests


parser = argparse.ArgumentParser(description="Task management system")
parser.add_argument('name_user', help='Name user')

args = parser.parse_args()

res = requests.get(f'https://api.github.com/users/{args.name_user}/events')

json = res.json()

if res.status_code == 200:
    print("User is found")
    print(json[0]['type'])
elif res.status_code == 404:
    print("User if not found")