import streamlit as st

st.set_page_config(page_title="Scholastic Hub | Stream", layout="wide")

# 2. HYBRID DESIGN CSS
st.markdown("""
<style>
    header, [data-testid="stHeader"] { display: none !important; }
    
    .stApp {
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
        color: #2c3e50;
    }

    [data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 40px !important;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        max-width: 1000px;
        margin: 40px auto !important;
    }

    .nav-link {
        color: #7f8c8d;
        font-weight: 500;
        padding: 10px 15px;
        border-radius: 12px;
        transition: 0.3s;
        cursor: pointer;
        display: inline-block;
        margin-right: 15px;
        text-decoration: none;
    }
    .nav-link-active {
        background: white;
        color: #2563eb;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    .notif-item {
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        border: 1px solid #f1f5f9;
        transition: transform 0.2s ease;
    }
    .notif-item:hover {
        transform: scale(1.01);
        border-color: #3b82f6;
    }

    .status-dot {
        height: 12px; width: 12px;
        background-color: #10b981; /* Green */
        border-radius: 50%;
        margin-right: 20px;
        box-shadow: 0 0 8px rgba(16, 185, 129, 0.4);
    }

    .stTextInput input {
        border-radius: 15px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <span class="nav-link">Dashboard</span>
        <span class="nav-link nav-link-active">Notifications</span>
        <span class="nav-link">Classwork</span>
        <span class="nav-link">Profile</span>
    </div>
""", unsafe_allow_html=True)

st.markdown('<h2 style="text-align: center; margin-bottom: 0;">Notifications</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #64748b; font-size: 14px;">Recent updates from your school portal</p>', unsafe_allow_html=True)


st.text_input("Search", placeholder="Search", label_visibility="collapsed")

notifications_api = []

if not notifications_api:
    st.markdown("""
        <div style="text-align: center; padding: 60px 0;">
            <div style="font-size: 50px; margin-bottom: 20px;">🕊️</div>
            <h4 style="color: #475569;">Your stream is empty</h4>
            <p style="color: #94a3b8; font-size: 14px;">Incoming data from the API will be listed here automatically.</p>
        </div>
    """, unsafe_allow_html=True)
else:
    for n in notifications_api:
        st.markdown(f"""
            <div class="notif-item">
                <div class="status-dot"></div>
                <div style="flex-grow: 1;">
                    <div style="display: flex; justify-content: space-between;">
                        <span style="font-weight: 600;">{n['title']}</span>
                        <span style="font-size: 12px; color: #94a3b8;">{n['time']}</span>
                    </div>
                    <div style="font-size: 14px; color: #64748b; margin-top: 4px;">{n['desc']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)