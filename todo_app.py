#!/usr/bin/env python3
"""Simple daily to-do list generator for scalp care and hair health."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Iterable


@dataclass(frozen=True)
class DailyTodo:
    day: date
    items: tuple[str, ...]


DEFAULT_ITEMS: tuple[str, ...] = (
    "Lower stress (10-minute walk, breathing, or stretch)",
    "Use Minoxidil as directed (daily)",
    "Gentle 2-minute scalp massage to support circulation",
    "Eat a protein-forward meal and hydrate well",
    "Sleep 7-8 hours and keep a consistent bedtime",
)


def add_months(start: date, months: int) -> date:
    """Return the date that is `months` after `start`, preserving day when possible."""
    target_month = start.month - 1 + months
    year = start.year + target_month // 12
    month = target_month % 12 + 1
    day = min(start.day, days_in_month(year, month))
    return date(year, month, day)


def days_in_month(year: int, month: int) -> int:
    """Return the number of days in a month."""
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    return (next_month - date(year, month, 1)).days


def iter_days(start: date, end: date) -> Iterable[date]:
    """Yield each day from start to end (inclusive)."""
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def build_daily_todos(start: date, months: int = 3) -> list[DailyTodo]:
    """Build daily to-dos from start date through the end of the period."""
    end = add_months(start, months) - timedelta(days=1)
    return [DailyTodo(day=day, items=DEFAULT_ITEMS) for day in iter_days(start, end)]


def format_todo(todo: DailyTodo) -> str:
    """Format a daily to-do into a friendly string."""
    header = todo.day.strftime("%B %d, %Y")
    lines = [f"{header}"]
    lines.extend(f"  - {item}" for item in todo.items)
    return "\n".join(lines)


def main() -> None:
    """Print the three-month daily to-do list starting January 1."""
    year = date.today().year
    start = date(year, 1, 1)
    todos = build_daily_todos(start)
    print(
        "Daily hair-care to-do list (3-month plan, January 1 start)\n"
        "================================================================"
    )
    for todo in todos:
        print(format_todo(todo))
        print()


if __name__ == "__main__":
    main()
