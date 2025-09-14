"""
    Expense Tracker project
"""

import os
import csv
import pandas as pd

if not os.path.exists("tracker.csv"):
    with open("tracker.csv","w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Date',"item","quantity","unit price","amount"])
else:
    print(f"File already exists")

class ExpenseTracker:

    def add_expense(self,date,item,quantity,unit_price,amount):
        with open("tracker.csv","a",newline="") as f:
            fieldnames = ['Date','item','quantity','unit price','amount']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow({
                "Date":date,
                "item":item,
                "quantity":quantity,
                "unit price":unit_price,
                "amount":amount
            })

    def view_expense(self):
        df = pd.read_csv("D:/AI Prep/Week 1/project_1/tracker.csv")
        return df

    def view_specific_expense(self,start_date,end_date):
        df = pd.read_csv("D:/AI Prep/Week 1/project_1/tracker.csv")
        # start_date,end_date = map(str,input("Enter the start date and end date in dd/mm/yy format respectively: ").split())
        df = df[(df['Date']>=start_date) & (df['Date']<=end_date)]
        return df


# expense = ExpenseTracker()
# expense.view_specific_expense()