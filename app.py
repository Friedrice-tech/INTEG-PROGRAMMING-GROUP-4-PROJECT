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

# --- POSTING PAGE ---
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
                st.success("Post live!")
            else:
                st.error("Missing name or content!")

# --- FEED PAGE ---
else:
    st.header("📢 Scholastic Feed")
    # Read the latest data
    df = pd.read_csv(DB_FILE)
    
    if df.empty:
        st.info("No posts yet.")
    else:
        # We loop through the index to target specific rows for editing
        # Reversing the index to show latest posts first
        for idx in reversed(df.index):
            row = df.iloc[idx]
            
            with st.container(border=True):
                col1, col2 = st.columns([0.85, 0.15])
                
                with col1:
                    st.subheader(f"{row['Author']} - {row['Category']}")
                    st.caption(f"Posted on: {row['Timestamp']}")
                
                with col2:
                    # Simple edit toggle for everyone
                    edit_mode = st.toggle("Edit", key=f"edit_{idx}")

                if edit_mode:
                    # Editable text area
                    new_content = st.text_area("Change message:", value=row['Content'], key=f"text_{idx}")
                    if st.button("Save Changes", key=f"save_{idx}"):
                        df.at[idx, 'Content'] = new_content
                        df.to_csv(DB_FILE, index=False)
                        st.success("Updated!")
                        st.rerun()
                else:
                    st.write(row['Content'])

                # --- FILE ACCESS ---
                if pd.notna(row['FileName']) and row['FileName'] != "":
                    file_path = os.path.join(UPLOAD_FOLDER, row['FileName'])
                    
                    if os.path.exists(file_path):
                        with open(file_path, "rb") as f:
                            st.download_button(
                                label=f"📂 Download {row['FileName']}",
                                data=f,
                                file_name=row['FileName'],
                                key=f"btn_{idx}" # Unique key for each button
                            )
                    else:
                        st.error("File not found on server.")