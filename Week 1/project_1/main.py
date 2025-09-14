from fastapi import FastAPI, Form
from pydantic import BaseModel
from backend import ExpenseTracker

my_expense = ExpenseTracker()

class Expense(BaseModel):
    date : str
    item : str
    quantity : int
    unit_price : int

class Date(BaseModel):
    start_date : str
    end_date : str

app = FastAPI()

@app.post('/add_expense',response_model = Expense)
def add_expense(date:str=Form(...),item:str=Form(...),quantity:int=Form(...),unit_price:int=Form(...)):
    amount = quantity * unit_price
    my_expense.add_expense(date,item,quantity,unit_price,amount)
    return Expense(date=date,item=item,quantity=quantity,unit_price=unit_price)

@app.get('/fetch')
def get_expense():
    df = my_expense.view_expense()
    return df.to_dict(orient="records")

@app.post('/fetch_specific')
def get_specific(dates:Date):
    df = my_expense.view_specific_expense(dates.start_date,dates.end_date)
    return df.to_dict(orient="records")
    
