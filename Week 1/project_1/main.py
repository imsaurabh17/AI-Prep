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

class update_value(BaseModel):
    date : str
    item : str
    updates : str

class delete_value(BaseModel):
    date : str
    item : str

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
    
@app.put('/update',response_model=update_value)
def update_values(date,item,updates):
    my_expense.update_expense(date,item,updates)
    return {"date":date,"item":item,"updates":updates}

@app.delete('/delete',response_model=delete_value)
def delete_value(date,item):
    my_expense.delete_expense(date,item)
    return {'date':date,'item':item}