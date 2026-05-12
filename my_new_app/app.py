import streamlit as st
from pages import profile, todo_list, lectures, dashboard # Import teammate files

# 1. Sidebar Navigation
st.sidebar.title("Scholastic Hub")
page = st.sidebar.radio("Menu", ["Dashboard", "Profile", "To-Do List", "Lecture Files"])

# 2. Logic to switch between files
if page == "Profile":
    profile.show()  # Calls the 'show' function in your profile.py
elif page == "To-Do List":
    todo_list.show()
elif page == "Lecture Files":
    lectures.show()
elif page == "Dashboard":
    dashboard.show() # Your teammate's code will run here