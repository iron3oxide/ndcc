from rich.console import Console

from ndcc import compare


def main():
    console = Console()
    tables = compare.get_tables()
    for table in tables:
        console.print(table)
