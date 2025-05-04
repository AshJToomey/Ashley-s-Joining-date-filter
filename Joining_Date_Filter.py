# Ashley's joining_date filter
import csv
from datetime import datetime

def load_workers(file_path):
    workers = []
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            workers.append(row)
    return workers

def filter_workers_by_date(workers, start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%d-%m-%y')
    end_date = datetime.strptime(end_date_str, '%d-%m-%y')

    filtered = []
    for worker in workers:
        joining_str = worker.get('Joining_date')  # match column exactly
        if not joining_str:
            print(f"Missing Joining_date in: {worker}")
            continue
        try:
            joining_date = datetime.strptime(joining_str, '%d/%m/%Y')  # correct format
            if start_date <= joining_date <= end_date:
                filtered.append({
                    'name': worker.get('Name'),
                    'joining_date': joining_date.strftime('%d-%m-%y')
                })
        except ValueError:
            print(f"Invalid date format in row: {worker}")
    return filtered

if __name__ == "__main__":
    workers = load_workers('workers.csv')
    filtered = filter_workers_by_date(workers, '01-04-23', '30-04-23')

    print("\nFiltered Workers Joining in April 2023:")
    for w in filtered:
        print(f"{w['name']} - {w['joining_date']}")
