# Ashley's joining_date filter
import csv
from datetime import datetime

def load_workers(file_path):
    workers = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            workers.append(row)
    return workers

def filter_workers_by_date(workers, start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%d-%m-%y')
    end_date = datetime.strptime(end_date_str, '%d-%m-%y')

    filtered = []
    for worker in workers:
        joining_date = datetime.strptime(worker['joining_date'], '%Y-%m-%d')
        if start_date <= joining_date <= end_date:
            filtered.append(joining_date.strftime('%d-%m-%y'))
    return filtered

if __name__ == "__main__":
    workers = load_workers('../data/workers.csv')
    filtered_dates = filter_workers_by_date(workers, '01-04-23', '30-04-23')
    print("Filtered Joining Dates (DD-MM-YY):")
    for date in filtered_dates:
        print(date)
