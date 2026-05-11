import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Files setup
DB_FILE = "scholastic_posts.csv"
UPLOAD_FOLDER = "shared_files"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize CSV if it doesn't exist
if not os.path.exists(DB_FILE):
    df = pd.DataFrame(columns=["Timestamp", "Author", "Category", "Content", "FileName"])
    df.to_csv(DB_FILE, index=False)

st.set_page_config(page_title="Scholastic Hub", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["View Feed", "Post Something"])

if page == "Post Something":
    st.header("📝 Share with ICS-401A")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Student Name")
        category = st.selectbox("Type", ["Reviewer", "Announcement", "Assignment", "General"])
        message = st.text_area("Details")
        file = st.file_uploader("Upload Document", type=['pdf', 'docx', 'pptx', 'png', 'jpg'])
        
        if st.form_submit_button("Share Now"):
            if name and (message or file):
                fname = file.name if file else ""
                if file:
                    with open(os.path.join(UPLOAD_FOLDER, fname), "wb") as f:
                        f.write(file.getbuffer())
                
                new_row = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M"), name, category, message, fname]], 
                                       columns=["Timestamp", "Author", "Category", "Content", "FileName"])
                new_row.to_csv(DB_FILE, mode='a', header=False, index=False)
                st.success("Post live on the Hub!")
            else:
                st.error("Missing name or content!")

else:
    st.header("📢 Scholastic Feed")
    df = pd.read_csv(DB_FILE)
    for _, row in df.iloc[::-1].iterrows():
        with st.container(border=True):
            st.subheader(f"{row['Author']} shared a {row['Category']}")
            st.caption(f"Posted on: {row['Timestamp']}")
            st.write(row['Content'])
            if row['FileName']:
                st.info(f"Attachment: {row['FileName']}")