# 🗂️ Ashley's Joining Date Filter

This is a simple desktop application built with Python and Tkinter that allows users to filter employees by their joining date from a CSV file. The app provides an intuitive graphical interface for selecting files and entering date ranges, then displays filtered results in a scrollable text box.

## **🖥️ Features**
- Upload a CSV file of employee data

- Input a start and end date (in dd-mm-yy format)

- Filter workers based on joining dates (from the Joining_date column)

- View filtered results in a scrollable, easy-to-read output box

- Handle invalid dates and missing fields gracefully

## **📂 Example CSV Format**
The CSV should contain at least the following columns:

Name,Joining_date
Alice Smith,01/04/2023
Bob Johnson,15/04/2023
Carol Lee,28/03/2023

⚠️ Joining_date must be in dd/mm/yyyy format (e.g. 01/04/2023).

## **🚀 How to Run**
1) Install Python
   Ensure Python 3 is installed on your system. You can download it from python.org.

2) Save the Script
   Save the code as joining_date_filter_gui.py.

3) Run the App
   Open a terminal or command prompt and run:

python joining_date_filter_gui.py

4) Use the GUI

-  Click Browse to select your .csv file

-  Enter a start and end date in dd-mm-yy format

-  Click Filter Workers to view results

## **🛠️ Dependencies**

This project only uses built-in Python libraries:

- csv

- datetime

- tkinter

No external packages required 🎉

## **📃 License**
This project is open-source and free to use under the MIT License.


