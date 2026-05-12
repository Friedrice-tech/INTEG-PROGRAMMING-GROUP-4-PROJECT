import streamlit as st

# 1. Page Config (Always first)
st.set_page_config(page_title="Scholastic Hub | Repo", layout="wide")

# 2. Combined CSS for Layout & Buttons
st.markdown("""
    <style>
    /* Card Styling */
    .lecture-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Prevent Download text from wrapping */
    .stDownloadButton button, .stButton button {
        white-space: nowrap !important;
        font-size: 14px !important;
        padding: 0px 5px !important;
    }

    /* Green Gradient for Download Button */
    .stDownloadButton > button {
        background: linear-gradient(90deg, #238636, #2ea043) !important;
        color: white !important;
        border: none !important;
    }

    /* Subtle Blue for View Button */
    div.stButton > button:first-child {
        border: 1px solid #30363d;
        background-color: #21262d;
    }
    </style>
    """, unsafe_allow_html=True)

def repo_page():
    st.title("📚 Lectures")
    st.write("Access and download your course materials.")
    st.divider()

    # Data Source
    lectures = [
        {"id": "L1", "title": "Lecture 1 - Introduction to BSIT", "date": "2023-01-15", "file": "Intro_BSIT.pdf"},
        {"id": "L2", "title": "Lecture 2 - Data Structure", "date": "2023-01-22", "file": "Data_Structures.pdf"},
        {"id": "L3", "title": "Lecture 3 - Algorithms", "date": "2023-01-22", "file": "Algorithms.pdf"},
    ]

    # Single Clean Loop
    for lec in lectures:
        # This 'with st.container(border=True)' creates the visual card
        with st.container(border=True):
            # Ratio 4:2:1:1 gives text the most room
            col1, col2, col3, col4 = st.columns([4, 2, 1.2, 1.2])
            
            with col1:
                st.markdown(f"**{lec['title']}**")
            
            with col2:
                st.caption(f"📅 {lec['date']}")
            
            with col3:
                # Real-time Download logic
                st.download_button(
                    label="Download",
                    data="This is where your file content goes", # Real use: open(file, 'rb').read()
                    file_name=lec['file'],
                    mime="application/pdf",
                    key=f"dl_btn_{lec['id']}", # Unique key
                    use_container_width=True
                )
                
            with col4:
                st.button("View", key=f"view_btn_{lec['id']}", use_container_width=True)

if __name__ == "__main__":
    repo_page()