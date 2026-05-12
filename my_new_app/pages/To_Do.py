import streamlit as st
from datetime import date
import time


if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Complete Project Proposal", "due": "2026-05-15", "status": "Pending"},
        {"id": 2, "title": "Study for Midterm Exam", "due": "2026-05-20", "status": "Pending"},
        {"id": 3, "title": "Read Chapter 3", "due": "2026-05-10", "status": "Completed"}
    ]

st.markdown("""
    <style>
    /* Sleek Input Fields */
    .stTextInput input, .stDateInput input {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        color: white !important;
    }

    /* Target the Checkmark Button (Green) */
    div.stButton > button:contains("✓") {
        color: #238636 !important;
        border: 1px solid #238636 !important;
        background-color: transparent !important;
        font-weight: bold;
    }
    div.stButton > button:contains("✓"):hover {
        background-color: #238636 !important;
        color: white !important;
    }

    /* Target the Delete Button (Red) */
    div.stButton > button:contains("🗑") {
        color: #f85149 !important;
        border: 1px solid #f85149 !important;
        background-color: transparent !important;
    }
    div.stButton > button:contains("🗑"):hover {
        background-color: #f85149 !important;
        color: white !important;
    }
    
    /* Primary Action Gradient for Add Task */
    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #58a6ff, #bc8cff) !important;
        border: none !important;
        font-weight: bold !important;
    }

    /* Custom Card Hover Effect */
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #58a6ff !important;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
head_left, head_right = st.columns([4, 1])
with head_left:
    st.header("✅ Scholastic Tracker")
with head_right:
    st.markdown("<div style='text-align: right; padding-top: 25px; color: #8b949e;'>👤 Student</div>", unsafe_allow_html=True)


with st.container(border=True):
    st.subheader("Add New Task")
    col_a, col_b = st.columns([3, 1])
    with col_a:
        new_title = st.text_input("Title", label_visibility="collapsed", placeholder="What needs to be done?")
    with col_b:
        new_date = st.date_input("Date", value=date.today(), label_visibility="collapsed")
    
    
    if st.button("Add Task", type="primary", use_container_width=True):
        if new_title:
            
            unique_id = int(time.time()) 
            st.session_state.tasks.append({
                "id": unique_id, 
                "title": new_title, 
                "due": str(new_date), 
                "status": "Pending"
            })
            st.rerun()
        else:
            st.error("Please enter a task title!")


st.write("### Pending Tasks")

for task in st.session_state.tasks[:]:
    if task["status"] == "Pending":
        with st.container(border=True):
            p_col1, p_col2, p_col3, p_col4 = st.columns([3, 1, 0.5, 0.5])
            with p_col1:
                st.write(f"**{task['title']}**")
            with p_col2:
                st.caption(f"📅 Due: {task['due']}")
            with p_col3:
                if st.button("✓", key=f"done_{task['id']}", use_container_width=True):
                    task["status"] = "Completed"
                    st.rerun()
            with p_col4:
                if st.button("🗑️", key=f"del_{task['id']}", use_container_width=True):
                    st.session_state.tasks.remove(task)
                    st.rerun()


st.write("---")
with st.expander("Show Completed Tasks"):
    for task in st.session_state.tasks[:]:
        if task["status"] == "Completed":
            c_col1, c_col2, c_col3 = st.columns([3, 1.5, 0.5])
            with c_col1:
                st.markdown(f"~~{task['title']}~~")
            with c_col2:
                st.caption(f"Completed: {task['due']}")
            with c_col3:
                if st.button("🗑️", key=f"del_comp_{task['id']}", use_container_width=True):
                    st.session_state.tasks.remove(task)
                    st.rerun()