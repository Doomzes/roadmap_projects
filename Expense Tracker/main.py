import argparse

class ExpenseTracker:
    def __init__(self):
        self.transactions = []


exp_track = ExpenseTracker()

parser = argparse.ArgumentParser(description="Task management system")
parser.add_argument('command', help='Name command')
parser.add_argument('--description', help='Description')
parser.add_argument('--amount', type=int, default=0, help='Amount')
args = parser.parse_args()
print(args)
