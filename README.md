# Personal Expense Tracker

A Python console application to record daily expenses by category and date, store them in a CSV file, and generate category-wise spending summaries using Pandas.

## Features
- Add expenses with input validation (YYYY-MM-DD date format and positive numeric amounts).
- Data persistence using CSV file storage (expenses.csv).
- Category-wise expenditure summaries and grand total calculation using Pandas groupby().
- View all recorded expenses in tabular format.

## Requirements
- Python 3
- Pandas library

## How to Run
1. Install pandas if not already installed:
   pip install pandas

2. Run the program:
   python expense_tracker.py