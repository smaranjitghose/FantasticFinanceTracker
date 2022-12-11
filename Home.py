import streamlit as st
import streamlit_lottie
from streamlit_option_menu import option_menu

import plotly.graph_objects as go
import calendar
from datetime import datetime
from deta import Deta 

from utils import *
import database as db

def main():
    """
    Main Function
    """
    st.set_page_config(
        page_title= "Fantastic Finance Tracker",
        page_icon = '💸',
        layout = "centered",
        menu_items={
        'Get Help': 'https://github.com/smaranjitghose/fantasticqrcode',
        'Report a bug': "https://github.com/smaranjitghose/fantasticqrcode/issues",
        'About': "## A minimalistic application to track income using python"
        }
    )
  
    st.title("Fantastic Finance Tracker💸")

    # Connect to Deta Base with your Project Key
    deta = Deta(st.secrets["deta_key"])

    # Access Desired Database
    db = deta.Base("financial_reports")


    hide_footer()
    # Load and display animation
    anim = lottie_local("assets/animations/money.json")
    st_lottie(anim,
            speed=2,
            reverse=False,
            loop=True,
            quality="medium", # low; medium ; high
            # renderer="svg", # canvas
            height=300,
            width=300,
            key=None,
            )


    # Define the attributes for Input Form
    income_sources = ["Developer Salary", "Freelance", "Consulting"]
    expense_areas = ["Rent","Electricity","Groceries","Personal Care","Travel","Cleaning","Data Plan","Mobile Plan"]
    currency = "INR"
    year_list = [2022,2023,2024]
    month_list = list(calendar.month_name)[1:]

    # Navigation Menu
    selected = option_menu(
                        menu_title=None,
                        options=["Data Entry", "Data Visualization"],
                        icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
                        orientation="horizontal")

    # Define Data Entry Tab 
    if selected == "Data Entry":
        st.header(f"Data Entry in {currency}")
        with st.form(key = "entry_form", clear_on_submit=True):
            # Create two columns
            left_c, right_c = st.columns(2)
            # Create select boxes in each of the columns for month and year
            left_c.selectbox("Choose Year:", year_list, key="year")
            right_c.selectbox("Choose Month:", month_list, key="month")
            "---" # Divider
            with st.expander("Income"):
                for i in income_sources:
                    st.number_input(f"{i}:", min_value=0, format="%i", step=10, key=i)
            with st.expander("Expenses"):
                for e in expense_areas:
                    st.number_input(f"{e}:", min_value=0, format="%i", step=10, key=e)
            "---" # Divider
            # Submit Button
            submitted = st.form_submit_button("Update Record")
            # If Client clicks on Submit button
            if submitted:
                period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
                incomes = {i: st.session_state[i] for i in income_sources}
                expenses = {e: st.session_state[e] for e in expense_areas}
                # Post data to desired database
                db.put({"key": period, "incomes": incomes, "expenses": expenses})
                st.success("Updated Records!")
                st.balloons()

    # Define Data Visualization Tab
    if selected == "Data Visualization":
        st.header("Data Visualization")
        with st.form(key = "saved_periods"):
            # Fetch all the periods for which user has financial data
            res = db.fetch()
            items = res.items
            periods = [item["key"] for item in items]
            # Allow the user to select a particular period
            period = st.selectbox("Select Period:", db.get_all_periods())
            submitted = st.form_submit_button("Show Finances")
            if submitted:
                # Get data from database
                period_data = db.get(period)
                comment = period_data.get("comment")
                expenses = period_data.get("expenses")
                incomes = period_data.get("incomes")

                # Display Fundamental financial Metrics for the period
                generate_finance_metrics(incomes, expenses,currency)
                # Display Sankey Chart for the period
                generate_finance_sankey(incomes,expenses)

def generate_finance_metrics(incomes,expenses,currency)->None:
    """
    Method to compute and display Total Income, Total Expense and Money Saved for a particular period
    """

    # Compute the desired metrics
    total_income = sum(incomes.values())
    total_expense = sum(expenses.values())
    remaining_budget = total_income - total_expense
    # Display the computed metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"{total_income} {currency}")
    col2.metric("Total Expense", f"{total_expense} {currency}")
    col3.metric("Remaining Budget", f"{remaining_budget} {currency}")

def generate_finance_sankey(incomes,expenses)->None:
        """
        Method to generate sankey chart
        """

        # Translate the given data into attributes for Sankey Chart Data Object
        label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
        source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
        target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
        value = list(incomes.values()) + list(expenses.values())

        # Create the dataobject for the Sankey Chart
        link = dict(source=source, target=target, value=value)
        node = dict(label=label, pad=20, thickness=30, color="#E694FF")
        data = go.Sankey(link=link, node=node)

        # Create the Sankey Chart Figure
        fig = go.Figure(data)
        # Adjust the Layout of the Sankey Chart
        fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
        # Plot the Sankey Chart Figure
        st.plotly_chart(fig, use_container_width=True)



if __name__ == "__main__":
    main()