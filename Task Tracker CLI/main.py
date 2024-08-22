import json
import os
from datetime import datetime
import argparse

class User:
    def __init__(self, f_name: str) -> None:
        self.now = now.strftime("%d/%m/%Y %H:%M:%S")
        self.f_name = f_name
        if not os.path.exists(self.f_name):
            with open(self.f_name, 'w') as file:
                json.dump({'1': {'description': '', 'status': '', 'createdAt': '', 'updatedAt': ''}}, file, indent=4)
        with open(self.f_name) as f:
            self.desc_list = json.load(f)
        self.id = [i for i in self.desc_list.keys()]
        self.last_id = int(list(self.desc_list.keys())[-1])

    def add_description(self, desc: str) -> None:
        self.last_id += 1
        self.desc_list[str(self.last_id)] = {'description': desc, 'status': 'in-progress', 'createdAt': self.now, 'updatedAt': self.now}
        with open(self.f_name, 'w') as f:
            json.dump(self.desc_list, f, indent=4)
        print("Successfully added")

    def update_description(self, id: str, desc: str) -> None:
        if str(id) in self.id:
            self.desc_list[str(id)].update({'description': desc, 'updatedAt': self.now})
            with open(self.f_name, 'w') as f:
                json.dump(self.desc_list, f, indent=4)
            print("Successfully update")
        else:
            print("This ID does not exist")

    def update_status(self, status: str, id: int) -> None:
        if str(id) in self.id:
            self.desc_list[str(id)].update({'status': status, 'updatedAt': self.now})
            with open(self.f_name, 'w') as f:
                json.dump(self.desc_list, f, indent=4)
            print("Successfully update status")
        else:
            print("This ID does not exist")

    def delete_description(self, id: str) -> None:
        if str(id) in self.id:
            del self.desc_list[str(id)]
            with open(self.f_name, 'w') as f:
                json.dump(self.desc_list, f, indent=4)
            print("Successfully delete")
        else:
            print("This ID does not exist")

    def list_task(self, name_list: str) -> None:
        print(f"|-------------------------------------All {name_list}-------------------------------------|\n")
        for i in self.desc_list:
            if self.desc_list[i]['status'] == f'{name_list}':
                print(f"id: {i}\n"
                      f"description: {self.desc_list[i]['description']}\n"
                      f"status: {self.desc_list[i]['status']}\n"
                      f"created: {self.desc_list[i]['createdAt']}\n"
                      f"updated: {self.desc_list[i]['updatedAt']}\n")
        print(f"|-------------------------------------All {name_list}-------------------------------------|\n")
    def all_task(self) -> None:
        print("|-------------------------------------All task-------------------------------------|\n")
        for i in self.desc_list:
            print(f"id: {i}\n"
                  f"description: {self.desc_list[i]['description']}\n"
                  f"status: {self.desc_list[i]['status']}\n"
                  f"created: {self.desc_list[i]['createdAt']}\n"
                  f"updated: {self.desc_list[i]['updatedAt']}\n")
        print("|-------------------------------------All task-------------------------------------|\n")


#определение текущего времени
now = datetime.now()

#подключение JSON файла
users = User('task.json')

#объявление аргументов для библиотек argparsе
parser = argparse.ArgumentParser(description="Task management system")
subparsers = parser.add_subparsers(dest='command', help="Commands")

#объявление паргументов для комманды 'update'
parser_update = subparsers.add_parser('update', help="Update a task")
parser_update.add_argument('task_id', type=int, help="ID of the task to update")
parser_update.add_argument('task_description', type=str, help="Description of the task")

#объявление аргументов для комманды 'add'
parser_add = subparsers.add_parser('add', help="Add a new task")
parser_add.add_argument('task_description', type=str, help="Description of the task")

#объявление аргументов для комманды 'delete'
parser_add = subparsers.add_parser('delete', help="Delete task")
parser_add.add_argument('task_id', type=int, help="ID of the task to delete")

#объявление аргументов для комманды 'mark-in-progress'
parser_add = subparsers.add_parser('mark-in-progress', help="Change task status on in progress")
parser_add.add_argument('task_id', type=int, help="Task ID to update status")

#объявление аргументов для комманды 'mark-in-progress'
parser_add = subparsers.add_parser('mark-done', help="Change task status on done")
parser_add.add_argument('task_id', type=int, help="Task ID to update status")

#объявление аргументов для комманды 'mark-in-progress'
parser_add = subparsers.add_parser('mark-todo', help="Change task status on todo")
parser_add.add_argument('task_id', type=int, help="Task ID to update status")

#объявление аргументов для комманды 'list'
parser_add = subparsers.add_parser('list', help="Show all tasks")
parser_add.add_argument('status', nargs='?', choices=['done', 'in-progress', 'todo'],
                        help="Filter tasks by their status (optional)")

args = parser.parse_args()

if __name__ == "__main__":
    if args.command == 'update':
        users.update_description(args.task_id, args.task_description)
    elif args.command == 'add':
        users.add_description(args.task_description)
    elif args.command == 'delete':
        users.delete_description(args.task_id)
    elif args.command == 'mark-in-progress':
        users.update_status('in-progress', args.task_id)
    elif args.command == 'mark-done':
        users.update_status('done', args.task_id)
    elif args.command == 'todo':
        users.update_status('todo', args.task_id)
    elif args.command == 'list':
        if args.status is None:
            users.all_task()
        else:
            users.list_task(args.status)
    else:
        parser.print_help()
