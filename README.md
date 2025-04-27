# **Ashley's Joining Date Filter** 🗂️

A simple Python script to filter worker joining dates from a CSV file based on a given date range. Useful for HR analytics, onboarding reports, and date-based filtering tasks.

📌 Features
Loads worker data from a CSV file
Filters workers by joining_date between two specified dates
Outputs dates in a readable DD-MM-YY format

🛠 Requirements
Python 3.x
CSV file with a joining_date column formatted as YYYY-MM-DD

📁 File Structure

├── filter_joining_dates.py

├── data/

│   └── workers.csv

📄 Sample Usage
Run the script using:
python filter_joining_dates.py

It will:

1) Load workers.csv from the data/ folder

2) Filter workers who joined between 01-Apr-2023 and 30-Apr-2023

3) Print matching dates in DD-MM-YY format

🧾 Sample CSV Format
name,joining_date
Alice,2023-04-10
Bob,2023-03-15
Charlie,2023-04-25

🔧 Customization
Modify the file_path or date range in if __name__ == "__main__": to fit your use case.

📜 License
MIT License

