"""Expense Tracker CLI Application"""
import json
from pathlib import Path
from argparse import ArgumentParser
from typing import TypeAlias, TypedDict

DatabaseRow = TypedDict(
    'DatabaseRow',
    {
        'id': int,
        'description': str,
        'amount': float,
        'category': str,
        'date': str,
    },
)

Database: TypeAlias = dict[str, list[DatabaseRow]]


def load_database(path: Path) -> Database:
    """Load the database from a JSON file"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'expenses': []}


def parse_args() -> ArgumentParser:
    """Parse command-line arguments"""
    parser: ArgumentParser = ArgumentParser(
        description='A CLI application to efficiently manage your Expenses',
        add_help=True, usage='expense-tracker <command> [options]')

    super_parser = parser.add_subparsers(
        title='Commands', dest='command', required=True, )
    super_parser.add_parser(
        'add', help='Add a new expense to the database')
    super_parser.add_parser(
        'list', help='List all expenses in the database')
    super_parser.add_parser(
        'summary', help='Remove an expense from the database')
    super_parser.add_parser(
        'delete', help='Update an expense in the database')

    return parser


def main():
    """Main function to run the CLI application"""

    print(f"{'=' * 50}")
    print(f"{' ' * 2}Expense Tracker CLI Application{' ' * 2}")
    print(f"{' ' * 2}type --help or -h to see all available commands{' ' * 2}")
    print(f"{'=' * 50}")

    parser = parse_args()
    args = parser

    user_command = ''
    while user_command != 'exit':
        user_command = input("expense-tracker ")
        if user_command in ('--help', '-h'):
            args.print_help()
            continue
        print(
            "Please enter a valid command. Type --help or -h to see all available commands.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Expense Tracker CLI Application. Goodbye!")
