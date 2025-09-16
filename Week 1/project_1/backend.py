"""
    Expense Tracker project
"""

import os
import csv
import pandas as pd
import ast

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

    def update_expense(self,date,item,updates,output_file='tracker.csv'):
        df = pd.read_csv("tracker.csv")
        mask = (df['Date']==date)&(df['item']==item)
        if not mask.any():
            print("No match found")
            return
        for col,new_val in ast.literal_eval(updates).items():
            if col in df.columns:
                df.loc[mask,col] = new_val
                df.loc[mask,'amount'] = df.loc[mask,'quantity']*df.loc[mask,'unit price']
            else:
                print(f"{col} not in csv file")

        if output_file:
            df.to_csv(output_file,index=False)
            print(f"Updated {output_file}")
        else:
            df.to_csv(output_file,index=False)
            print(f"Created {output_file}")
        
    def delete_expense(self,date,item,output_file='tracker.csv'):
        df = pd.read_csv("tracker.csv")
        mask = (df['Date']==date)&(df['item']==item)
        if not mask.any():
            print("No matches found")
            return
        
        df.drop(df[mask].index,inplace=True)

        df.to_csv(output_file,index=False)
        
