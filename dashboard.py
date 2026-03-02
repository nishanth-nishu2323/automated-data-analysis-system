import streamlit as st
import pandas as pd
import mysql.connector

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Automated Data Analysis Dashboard",
    layout="wide"
)

# ------------------ MYSQL CONNECTION ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nishu@2328",
    database="automated_analysis"
)

# Load tables
users = pd.read_sql("SELECT * FROM users", conn)
products = pd.read_sql("SELECT * FROM products", conn)
orders = pd.read_sql("SELECT * FROM orders", conn)

# ------------------ SIDEBAR ------------------
st.sidebar.title("Select Data")

option = st.sidebar.selectbox(
    "",
    ["Users", "Products", "Orders", "Reports"]
)

# ------------------ MAIN TITLE ------------------
st.markdown(
    "<h1 style='text-align:center;'>📊 Automated Data Analysis Dashboard</h1>",
    unsafe_allow_html=True
)

st.write("")  # spacing

# ------------------ CONTENT ------------------
if option == "Users":
    st.subheader("Users Data")
    st.dataframe(users, use_container_width=True)

elif option == "Products":
    st.subheader("Products Data")
    st.dataframe(products, use_container_width=True)

elif option == "Orders":
    st.subheader("Orders Data")
    st.dataframe(orders, use_container_width=True)

elif option == "Reports":
    st.subheader("Summary Report")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Users", users.shape[0])
    col2.metric("Total Products", products.shape[0])
    col3.metric("Total Orders", orders.shape[0])

# ------------------ CLOSE CONNECTION ------------------
conn.close()