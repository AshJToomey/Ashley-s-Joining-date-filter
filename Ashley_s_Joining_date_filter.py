# Ashley's joining_date filter
import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def load_workers(file_path):
    workers = []
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            workers.append(row)
    return workers

def filter_workers_by_date(workers, start_date_str, end_date_str):
    try:
        start_date = datetime.strptime(start_date_str, '%d-%m-%y')
        end_date = datetime.strptime(end_date_str, '%d-%m-%y')
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter dates in dd-mm-yy format.")
        return []

    filtered = []
    for worker in workers:
        joining_str = worker.get('Joining_date')
        if not joining_str:
            continue
        try:
            joining_date = datetime.strptime(joining_str, '%d/%m/%Y')
            if start_date <= joining_date <= end_date:
                filtered.append({
                    'name': worker.get('Name'),
                    'joining_date': joining_date.strftime('%d-%m-%y')
                })
        except ValueError:
            continue
    return filtered

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

def run_filter():
    file_path = file_entry.get()
    start_date = start_entry.get()
    end_date = end_entry.get()

    try:
        workers = load_workers(file_path)
    except Exception as e:
        messagebox.showerror("File Error", f"Could not load file:\n{e}")
        return

    results = filter_workers_by_date(workers, start_date, end_date)
    output_text.delete(1.0, tk.END)
    if results:
        for worker in results:
            output_text.insert(tk.END, f"{worker['name']} - {worker['joining_date']}\n")
    else:
        output_text.insert(tk.END, "No workers found in the given date range.")

# --- GUI Layout ---
root = tk.Tk()
root.title("Joining Date Filter")
root.geometry("600x400")
root.resizable(False, False)

tk.Label(root, text="CSV File:").pack(pady=(10, 0))
file_frame = tk.Frame(root)
file_frame.pack(padx=10, pady=5, fill='x')
file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side='left', fill='x', expand=True)
tk.Button(file_frame, text="Browse", command=browse_file).pack(side='right')

date_frame = tk.Frame(root)
date_frame.pack(padx=10, pady=10, fill='x')
tk.Label(date_frame, text="Start Date (dd-mm-yy):").grid(row=0, column=0, sticky='e')
start_entry = tk.Entry(date_frame, width=15)
start_entry.grid(row=0, column=1, padx=5)

tk.Label(date_frame, text="End Date (dd-mm-yy):").grid(row=0, column=2, sticky='e')
end_entry = tk.Entry(date_frame, width=15)
end_entry.grid(row=0, column=3, padx=5)

tk.Button(root, text="Filter Workers", command=run_filter).pack(pady=5)

output_text = scrolledtext.ScrolledText(root, height=12, width=70)
output_text.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()
