import streamlit as st 
from deta import Deta  
from dotenv import load_dotenv
import os

# ------ Use this for testing in local system -------
# # Load the environment variables file
# load_dotenv(".env")
# # Read the value for DETA Key
# project_key = os.getenv("DETA_KEY")

# ------ Use this for streamlit sharing/Heroku -------
project_key = st.secrets("DELTA_KEY")


# Connect to the DETA Project
deta = Deta(project_key)
# Access/Create a Database
db = deta.Base("financial_reports")


def submit_finance_data(period:str, incomes:dict, expenses:dict)->None:
    """
    Method to push the entries for a particular month to the database
    """
    db.put({"key": period, "incomes": incomes, "expenses": expenses})


def get_period(period:str):
    """
    Function to get the entries for a particular period
    """
    return db.get(period)

def get_all_periods():
    """
    Function to fetch all periods in the database
    """
    res = db.fetch()
    items = res.items
    periods = [item["key"] for item in items]
    return periods