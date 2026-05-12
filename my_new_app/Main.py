import streamlit as st


st.set_page_config(page_title="Scholastic Hub", layout="wide")


st.markdown("""
    <style>
    /* Targeting the title specifically */
    .hero-title {
        font-size: 80px !important; /* Adjust this number to go even bigger */
        font-weight: 900;
        letter-spacing: -2px;
        line-height: 1;
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: -20px;
        margin-bottom: 10px;
        filter: drop-shadow(0px 5px 15px rgba(88, 166, 255, 0.3));
    }
    
    /* Subtitle styling */
    .hero-subtitle {
        font-size: 20px;
        color: #8b949e;
        margin-bottom: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="hero-title">Scholastic Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Scholastic Hub: Your Academic buddy.</p>', unsafe_allow_html=True)

# --- HEADER SECTION ---

st.markdown("Welcome back! Here is a quick overview of your academic progress.")
st.divider()

# --- TOP STATS (Metrics) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Active Courses", value="5", delta="2 New")
with col2:
    st.metric(label="Pending Tasks", value="12", delta="-3", delta_color="normal")
with col3:
    st.metric(label="Current GWA", value="1.25", delta="+0.05")
with col4:
    st.metric(label="Days to Finals", value="14", delta_color="off")

st.write("##") # Spacer


left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📌 Recent Activity")
    with st.container(border=True):
        st.write("**Quantitative Methods- Discrete Probability:** New lecture notes uploaded.")
        st.caption("2 hours ago")
        st.divider()
        st.write("**Integrative Programming Project-** Successfully pushed to GitHub.")
        st.caption("Yesterday")

with right_col:
    st.subheader("📅 Upcoming Deadlines")
    st.info("**Graphics Quiz:** Tomorrow at 10:00 AM")
    st.warning("**Final Project:** Friday at 11:59 PM")