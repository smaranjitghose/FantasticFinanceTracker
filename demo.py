from deta import Deta 
import streamlit as st

# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
# Access Desired Database
db = deta.Base("financial_reports")
res = db.fetch()
# items = res.items
# periods = [item["key"] for item in items]
print(res.items)