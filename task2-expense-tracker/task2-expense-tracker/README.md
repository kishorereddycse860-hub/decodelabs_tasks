# Task 2: Expense Tracker

A simple command-line Expense Tracker app built in Python.

## Features
- Add expense amounts one at a time
- Automatically keeps a running total
- Handles invalid input gracefully
- Shows a summary of total expenses and count when finished

## How to Run
python expense_tracker.py

## How it Works
1. Enter an expense amount when prompted
2. Keep entering amounts one by one — the running total updates after each entry
3. Type 'done' when you want to stop
4. A summary is displayed showing total expenses entered and total amount spent

## Example
===== EXPENSE TRACKER =====
Enter an expense amount to add it to your total
Type 'done' when you want to stop and see your total
Enter expense amount (or 'done' to finish): 100
Added $100.00. Running total: $100.00

Enter expense amount (or 'done' to finish): 50.5
Added $50.50. Running total: $150.50

Enter expense amount (or 'done' to finish): done
===== SUMMARY =====
Total expenses entered: 2
Total Spent: $150.50

## Tech Used
- Python 3 (input handling, exception handling with try/except, f-strings)
