import streamlit as st
from datetime import date, time
import pandas as pd
import random

# -- Page Config --
st.set_page_config(
    page_title="Student Productivity Tracker",
    page_icon="🎓",
    layout="wide"
)

# -- Sidebar Navigation --
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Tracker", "Achievements", "Tips", "About"])

# -- HOME PAGE --
if page == "Home":
    st.title("🎓 Student Productivity Tracker")
    st.header("Welcome!")
    st.subheader("Track your study habits and productivity with ease")
    
    st.info(
        """
        This app helps you monitor your **study hours**, **mood**, and **skills practiced**.
        Use it daily to stay motivated and improve your productivity!
        """
    )
    
    st.write("Here’s what you can do on this app:")
    st.markdown("""
    - Log your study hours 🕒  
    - Track your mood and motivation 😊  
    - Record skills practiced 🎯  
    - Get feedback and see your progress 📊  
    - Earn achievements and badges 🏆
    """)
    
    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80",
        caption="Stay focused and motivated!",
        use_column_width=True
    )
    st.video("https://www.youtube.com/watch?v=rfscVS0vtbw")
    st.balloons()

# -- TRACKER PAGE --
elif page == "Tracker":
    st.title("📊 Study Tracker")

    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", 10, 100)
        favorite_subject = st.selectbox(
            "Favorite Subject", ["Math", "Programming", "Science", "History"]
        )
        mood = st.radio("Mood today", ["Happy", "Neutral", "Tired", "Stressed"])
        skills = st.multiselect(
            "Skills you practiced today",
            ["Coding", "Writing", "Problem Solving", "Reading", "Drawing", "Public Speaking"]
        )
    
    with col2:
        study_hours = st.slider("Hours studied today", 0, 12)
        reminder = st.checkbox("Enable study reminder")
        study_date = st.date_input("Study Date", date.today())
        study_time = st.time_input("Study Time", time(hour=9, minute=0))
        color_theme = st.color_picker("Pick your theme color", "#00f900")
        uploaded_file = st.file_uploader(
            "Upload your study notes (optional)", type=["txt", "pdf", "jpg", "png"]
        )
    
    with st.expander("Additional Notes"):
        notes = st.text_area("Write any notes or reflections here:")
    
    if st.button("Calculate Productivity"):
        # Productivity scoring
        score = study_hours * 10 + len(skills) * 5
        st.metric("Productivity Score", score)
        st.progress(min(score / 100, 1.0))
        
        if score >= 80:
            st.success(f"Excellent productivity today, {name}! Keep it up!")
            st.balloons()
        elif score >= 50:
            st.info(f"Good job, {name}. You are doing well!")
        else:
            st.warning(f"Don't worry, {name}. Try to study a bit more tomorrow!")
        
        summary_data = {
            "Name": [name],
            "Age": [age],
            "Study Hours": [study_hours],
            "Mood": [mood],
            "Favorite Subject": [favorite_subject],
            "Skills Practiced": [', '.join(skills)],
            "Date": [study_date],
            "Time": [study_time],
        }
        df = pd.DataFrame(summary_data)
        st.table(df)

# -- ACHIEVEMENTS PAGE --
elif page == "Achievements":
    st.title("🏆 Achievements")
    st.write("Here you can see milestones and badges for your study progress!")
    
    # Example badges
    streak_days = random.randint(0, 10)
    total_hours = random.randint(0, 50)
    
    st.markdown(f"**Daily Streak:** 🔥 {streak_days} days in a row")
    st.markdown(f"**Hours Studied This Week:** ⏰ {total_hours} hours")
    
    # Fun animation for achievements
    if streak_days >= 5:
        st.balloons()
    
    st.markdown("""
    - Earn badges by maintaining streaks  
    - Unlock achievements for studying multiple skills  
    - Keep track of your productivity over time
    """)

# -- TIPS PAGE --
elif page == "Tips":
    st.title("💡 Study Tips & Motivation")
    tips = [
        "Remember to take a break.",
        "Review your notes daily.",
        "Set realistic study goals.",
        "Practice active recall.",
        "Stay hydrated and rest well."
    ]
    
    st.write("Here are some helpful study tips for students:")
    
    for tip in tips:
        st.info(f"✅ {tip}")
    
    quote = "“The secret of getting ahead is getting started.” – Mark Twain"
    st.success(f"Inspirational Quote: {quote}")

# -- ABOUT PAGE --
elif page == "About":
    st.title("ℹ️ About Student Productivity Tracker App")
    
    st.header("🎯 Use Case")
    st.write(
        "This app helps students **track study time, mood, and skills** to monitor productivity, "
        "receive feedback, and improve study habits over time."
    )
    
    st.header("👥 Target Users")
    st.write(
        "Designed for **college and high school students** who want to keep track of their study sessions, "
        "measure productivity, and stay motivated with interactive feedback."
    )
    
    st.header("📝 Inputs Collected")
    st.markdown("""
- **Name**  
- **Age**  
- **Study hours** (slider input)  
- **Mood** (radio buttons)  
- **Favorite subject** (dropdown)  
- **Skills practiced** (multi-select)  
- **Date and time of study** (date & time picker)  
- **Color preference** (color picker)  
- **File uploads** (optional)  
- **Reminder toggle** (checkbox)  
- **Additional notes** (text area)
    """)
    
    st.header("📊 Outputs Shown")
    st.markdown("""
- **Productivity score** (numeric metric)  
- **Progress bar** (visual representation of completion)  
- **Motivational messages & animations** (balloons/snow)  
- **Summary table** (with all user inputs for reference)
    """)
    
    st.info("💡 Tip: Use this app daily to track your study habits and improve productivity over time!")
