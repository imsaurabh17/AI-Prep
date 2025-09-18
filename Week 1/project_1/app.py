import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/"

st.title("Expense Tracker System")

menu = ['Add','View','View_specific','Update','Delete']

choice = st.sidebar.selectbox("Menu",menu)

# Add

if choice == "Add":
    st.subheader("Add expense")
    date = st.text_input("Date in dd/mm/yyyy")
    item = st.text_input("Name of the item")
    quantity = st.number_input("Number of item purchased")
    unit_price = st.number_input("Price of 1 item")
    amount = quantity * unit_price

    if st.button("Add Expense"):
        payload = {
            "date":date,
            "item":item,
            "quantity":quantity,
            "unit_price":unit_price
        }
        response = requests.post(f"{API_URL}/add_expense",params=payload)
        if response.status_code == 200:
            st.write("Expense added")
        else:
            st.write("Failed to add expense")

elif choice == "View":
    response = requests.get(f"{API_URL}/fetch")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("No data available")

elif choice == "View_specific":
    start_date = st.text_input("Enter start date")
    end_date = st.text_input("Enter end date")
    if st.button("View Expense"):
        payload = {
            "start_date":start_date,
            "end_date":end_date
        }
        response = requests.post(f"{API_URL}/fetch_specific",json=payload)
        if response.status_code == 200:
            data = response.json()
            if not data:
                st.warning("No available data for this date range")
            else:
                df = pd.DataFrame(data)
                st.dataframe(df)
        else:
            st.write("Enter correct date")

elif choice == "Update":
    date = st.text_input("Enter the date")
    item = st.text_input("Enter the item name")
    updates = st.text_input("Write the data to update with column names and corresponding values in key:value pair")
    if st.button("Update"):
        payload = {
            'date':date,
            'item':item,
            'updates':updates
        }
        response = requests.put(f"{API_URL}/update",json=payload)
        if response.status_code == 200:
            st.write("Date updated")
        else:
            st.write("No such data found")