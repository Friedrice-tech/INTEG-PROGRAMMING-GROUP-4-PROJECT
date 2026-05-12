import streamlit as st


st.markdown("""
    <style>
    .profile-pic {
        width: 150px;
        height: 150px;
        background-color: #d1d5db;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


head_left, head_right = st.columns([4, 1])
with head_left:
    st.header("Student Profile")
with head_right:
    st.markdown("<div style='text-align: right; padding-top: 10px;'>👤 Student</div>", unsafe_allow_html=True)


with st.container(border=True):
   
    img_col, info_col = st.columns([1, 3])
    
    with img_col:
        
        st.markdown('<div class="profile-pic"></div>', unsafe_allow_html=True)
        
        st.button("Edit Profile", type="primary")
        
    with info_col:
        
        st.write("## Student Name")
        st.write("institutionalemail@rtu.edu.ph")
        st.write("**Status:** Enrolled")