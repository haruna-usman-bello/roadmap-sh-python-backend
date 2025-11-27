"""Expense Tracker CLI Application"""
import json
from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from typing import TypeAlias, TypedDict

DatabaseRow = TypedDict(
    'DatabaseRow',
    {
        'id': int,
        'description': str,
        'amount': float,
        'date': str,
    },
)

Database: TypeAlias = list[DatabaseRow]


def load_database(path: Path) -> Database:
    """Load the database from a JSON file"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


database: Database = load_database(Path('expenses.json'))


def add_expense(description: str, amount: float, date: str) -> None:
    """Add a new expense to the database"""
    database.append({
        'id': len(database) + 1,
        'description': description,
        'amount': amount,
        'date': date,
    })

    with open('expenses.json', 'w', encoding='utf-8') as file:
        json.dump(database, file, indent=2)


def list_expenses() -> None:
    """List all expenses in the database"""
    if not database:
        print('No expenses found in the database.')
    for expense in database:
        print(
            f"{expense['id']}: {expense['description']} - ${expense['amount']}  on {expense['date']}")


# Main Argument Parser
parser = ArgumentParser(description='A CLI application to efficiently manage your Expenses',
                        add_help=True, usage='expense-tracker <command> [options]')

# Subparsers for different commands
subparsers = parser.add_subparsers(
    title='Commands', dest='command', required=True, )

# Create subparser for 'add' command with arguments
add_parser = subparsers.add_parser(
    'add', help='Add a new expense to the database', usage='expense-tracker add <category> <description> <amount>')
add_parser.add_argument('--description', required=True,
                        type=str, help='Description of the expense')
add_parser.add_argument('--amount', required=True,
                        type=float, help='Amount of the expense')

# create subparser for 'list' command
list_parser = subparsers.add_parser(
    'list', help='List all expenses in the database')

# create subparser for 'summary' command
summary_parser = subparsers.add_parser(
    'summary', help='Remove an expense from the database')

# create subparser for 'delete' command
delete_parser = subparsers.add_parser(
    'delete', help='Update an expense in the database')


def main():
    """Main function to run the CLI application"""

    args = parser.parse_args()

    match args.command:
        case 'add':
            add_expense(
                description=args.description,
                amount=args.amount,
                date=datetime.now().strftime('%Y-%m-%d'))
        case 'list':
            list_expenses()
        case 'summary':
            print("Showing summary of expenses...")
        case 'delete':
            print("Deleting an expense...")
        case _:
            parser.print_help()


if __name__ == '__main__':

    main()
