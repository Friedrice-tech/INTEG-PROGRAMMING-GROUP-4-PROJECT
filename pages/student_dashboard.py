import streamlit as st

# 1. Page Configuration matching the template
st.set_page_config(page_title="Scholastic Hub - Student Dashboard", layout="wide")

# Inject Custom CSS to replicate the layout, metrics cards, and color scheme
st.markdown("""
    <style>
    /* Main Background and Font */
    .stApp {
        background-color: #F8F9FA;
    }
    html, body, [class*="css"] {
        font-family: 'Segoe UI', system-ui, sans-serif;
    }
    
    /* Header Block Typography */
    .univ-title {
        color: #F2A900; /* Gold/Orange brand color */
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: -5px;
    }
    .page-title {
        color: #0A2540; /* Dark Navy brand color */
        font-size: 32px;
        font-weight: 700;
        margin-top: 0px;
        margin-bottom: 5px;
    }
    .page-subtitle {
        color: #6C757D;
        font-size: 14px;
        margin-bottom: 15px;
    }
    .color-bar {
        width: 60px;
        height: 4px;
        background: linear-gradient(to right, #0A2540, #F2A900);
        border-radius: 2px;
        margin-bottom: 30px;
    }
    
    /* Metadata Sidebar Block */
    .meta-box {
        background-color: #FFFFFF;
        border: 1px solid #E9ECEF;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.02);
    }
    .meta-item {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
        font-size: 13px;
    }
    .meta-label {
        color: #6C757D;
    }
    .meta-value {
        font-weight: 600;
        color: #0A2540;
    }
    
    /* Top row mini metric cards */
    .metric-card {
        background-color: #FFFFFF;
        border-top: 4px solid #0A2540;
        border-radius: 4px 4px 12px 12px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        border-left: 1px solid #E9ECEF;
        border-right: 1px solid #E9ECEF;
        border-bottom: 1px solid #E9ECEF;
    }
    .metric-title {
        font-size: 13px;
        color: #495057;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: 700;
        color: #0A2540;
    }
    
    /* Main Shortcut Container Blocks */
    .dashboard-card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #E9ECEF;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        margin-bottom: 25px;
        height: 100%;
    }
    .card-heading {
        color: #0A2540;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 15px;
        border-bottom: 2px solid #F1F3F5;
        padding-bottom: 8px;
    }
    
    /* Quick Alert Elements */
    .alert-text {
        font-size: 13px;
        color: #495057;
        padding: 6px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Top Header Layout
header_col, meta_col = st.columns([2.5, 1])

with header_col:
    st.markdown('<p class="univ-title">Rizal Technological University</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-title">Student Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Second Semester AY 2025-2026</p>', unsafe_allow_html=True)
    st.markdown('<div class="color-bar"></div>', unsafe_allow_html=True)

with meta_col:
    st.markdown("""
        <div class="meta-box">
            <div class="meta-item"><span class="meta-label">Program:</span><span class="meta-value">BSIT</span></div>
            <div class="meta-item"><span class="meta-label">Block Section:</span><span class="meta-value">401A</span></div>
            <div class="meta-item"><span class="meta-label">Year Level:</span><span class="meta-value">2nd Year</span></div>
            <div class="meta-item"><span class="meta-label">Semester Status:</span><span class="meta-value">Enrolled</span></div>
        </div>
    """, unsafe_allow_html=True)

# 3. Overview Analytics Metrics Row (Matching the 4 blocks structure from your layout)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="metric-card"><div class="metric-title">Total Subjects</div><div class="metric-value">9</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><div class="metric-title">Total Units</div><div class="metric-value">23</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><div class="metric-title">Laboratory Classes</div><div class="metric-value">4</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-card"><div class="metric-title">Class Days</div><div class="metric-value">3</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. Main Grid Section: Shortcuts & Quick Previews
col_left, col_right = st.columns([1.8, 1.2])

with col_left:
    # --- SHORTCUT 1: CLASS SCHEDULE PREVIEW ---
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<p class="card-heading">📅 Class Schedule Today</p>', unsafe_allow_html=True)
    
    # Simple interactive display showing immediate scheduled items
    sched_data = [
        {"Time": "7:00 AM - 9:00 AM", "Subject": "ITP221 - Networking 1", "Room": "E501"},
        {"Time": "10:00 AM - 12:00 PM", "Subject": "ITP222 - Integrative Programming", "Room": "E409"}
    ]
    st.table(sched_data)
    
    if st.button("Open Full Schedule Viewer ➔", key="go_sched"):
        st.info("Redirecting to Full Class Schedule Page...")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SHORTCUT 2: LECTURE FILES SHORTCUT ---
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<p class="card-heading">📂 Recent Lecture Files</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="alert-text">📄 <b>Networking_Ch3_Subnetting.pdf</b> (Uploaded today)</p>', unsafe_allow_html=True)
    st.markdown('<p class="alert-text">📄 <b>Integrative_Prog_Lab2.zip</b> (Uploaded yesterday)</p>', unsafe_allow_html=True)
    
    if st.button("Browse Lecture Repository ➔", key="go_files"):
        st.info("Redirecting to Lecture Files Repository...")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # --- SHORTCUT 3: TO-DO LIST PREVIEW ---
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<p class="card-heading">📋 Pending To-Do List</p>', unsafe_allow_html=True)
    
    st.checkbox("Submit Networking Activity 3", value=False)
    st.checkbox("Review Integrative Programming Notes", value=False)
    st.checkbox("Read Chapter 4 Lecture Slides", value=True) # Checked means done
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Manage All Assignments ➔", key="go_todo"):
        st.info("Redirecting to Assignment Tracker...")
    st.markdown('</div>', unsafe_allow_html=True)
