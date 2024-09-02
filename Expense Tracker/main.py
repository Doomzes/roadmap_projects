import argparse
import csv
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self) -> None:
        self.now = now.strftime("%d/%m/%Y %H:%M:%S")
        self.header = []
        self.transactions = []
        self.f_name = 'sw_data.csv'
        self.id = []
        if not os.path.exists(self.f_name):
            with open(self.f_name, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["ID", "Data", "Description", "Amount"]
                )
        with open(self.f_name, "r", newline='') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if lines[0] == "ID":
                    self.header.append(lines)
                else:
                    self.transactions.append(lines)
                    self.id.append(lines[0])
        self.last_id = int(self.id[-1])

    def add_expense(self, desc: str, amount: int) -> None:
        self.last_id += 1
        with open(self.f_name, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [self.last_id, self.now[:10], desc, amount]
            )
        print(f"Expense added successfully (ID: {self.last_id})")

    def list_expense(self):
        print(self.transactions)
        header = (f"{f'{self.header[0][0]}':<4} {f'{self.header[0][1]}':<12} {f'{self.header[0][2]}':<20} "
                  f"{f'{self.header[0][3]}':<10}")
        print(header)
        print("-" * len(header))

        for transaction in self.transactions:
            print(f"{f'{self.transactions[0][0]}':<4} {f'{self.transactions[0][1]}':<12} {f'{self.transactions[0][2]}':<20}"
                  f"{f'{self.transactions[0][3]}':<10}")


#определение текущего времени
now = datetime.now()

exp_track = ExpenseTracker()

parser = argparse.ArgumentParser(description="Task management system")
subparsers = parser.add_subparsers(dest='command', help="Commands")

#объявление паргументов для комманды 'add'
parser_update = subparsers.add_parser('add', help="Expense added")
parser_update.add_argument('--description', help='Description')
parser_update.add_argument('--amount', type=int, default=0, help='Amount')

#объявление паргументов для комманды 'list'
parser_update = subparsers.add_parser('list', help="Shows expenses in tabular form")
parser_update.add_argument('--month', type=int, help='To display the amount of expenses for the specified month')

#объявление паргументов для комманды 'summary'
parser_update = subparsers.add_parser('summary', help="Calculates the total amount of expenses")
parser_update.add_argument('--month', type=int, help='To display the amount of expenses for the specified month')

#объявление паргументов для комманды 'delete'
parser_update = subparsers.add_parser('delete', help="Deletes the entry")
parser_update.add_argument('--id', type=int, help='the entry is deleted by the specified ID')

args = parser.parse_args()

if __name__ == "__main__":
    if args.command == 'add':
        exp_track.add_expense(args.description, args.amount)
    elif args.command == 'list':
        exp_track.list_expense()