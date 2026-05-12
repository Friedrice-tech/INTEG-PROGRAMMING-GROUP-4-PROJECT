import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Scholastic Hub - Class Representative",
    page_icon="📚",
    layout="wide"
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.title("📚 Scholastic Hub")
st.subheader("Class Representative Dashboard")

st.write(
    "A centralized dashboard for communication, monitoring, "
    "student concerns, and academic tracking."
)

st.divider()

# ---------------------------------------------------
# SIDEBAR PROFILE
# ---------------------------------------------------
st.sidebar.header("👤 Class Representative")

st.sidebar.write("### Jerome Luz")
st.sidebar.write("📧 jerome@classmail.com")
st.sidebar.write("📱 0912-345-6789")
st.sidebar.write("🕒 Available: 1:00 PM - 4:00 PM")

st.sidebar.info(
    "Students may contact the Class Representative "
    "for concerns and academic updates."
)

# ---------------------------------------------------
# PERFORMANCE METRICS
# ---------------------------------------------------
st.header("📊 Performance Metrics Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Attendance Rate", "92%")

with col2:
    st.metric("Assessment Completion", "85%")

with col3:
    st.metric("Student Engagement", "88%")

st.divider()

# ---------------------------------------------------
# FEEDBACK / SURVEY
# ---------------------------------------------------
st.header("🗳️ Feedback / Survey Mechanism")

st.write("Poll: Should the Networking exam be moved next week?")

survey = st.radio(
    "Select your answer:",
    ["Yes", "No", "Maybe"]
)

if st.button("Submit Survey"):
    st.success(f"Your answer '{survey}' has been submitted.")

feedback = st.text_area(
    "Submit anonymous feedback or suggestions"
)

if st.button("Send Feedback"):
    if feedback:
        st.success("Feedback submitted successfully!")
    else:
        st.warning("Please type feedback first.")

st.divider()

# ---------------------------------------------------
# DEADLINE TRACKER
# ---------------------------------------------------
st.header("📌 Syllabus / Deadline Tracker")

deadlines = pd.DataFrame({
    "Subject": [
        "Networking",
        "Research",
        "Programming",
        "Database"
    ],
    "Task": [
        "Router Configuration",
        "Proposal Defense",
        "Streamlit Dashboard",
        "Normalization Activity"
    ],
    "Deadline": [
        "May 15",
        "May 18",
        "May 20",
        "May 22"
    ],
    "Status": [
        "Pending",
        "Ongoing",
        "Submitted",
        "Pending"
    ]
})

st.dataframe(deadlines, use_container_width=True)

st.divider()

# ---------------------------------------------------
# EVENT SCHEDULING
# ---------------------------------------------------
st.header("📅 Event Scheduling Integration")

events = pd.DataFrame({
    "Event": [
        "Class Representative Meeting",
        "Student-Faculty Consultation",
        "Research Orientation",
        "Mock Defense"
    ],
    "Date": [
        "May 14",
        "May 16",
        "May 19",
        "May 23"
    ],
    "Time": [
        "2:00 PM",
        "1:00 PM",
        "10:00 AM",
        "9:00 AM"
    ]
})

st.table(events)

st.divider()

# ---------------------------------------------------
# ACTION TRACKING LOG
# ---------------------------------------------------
st.header("📋 Action Tracking Log")

issues = pd.DataFrame({
    "Concern": [
        "Projector not working",
        "Request for exam reschedule",
        "Missing laboratory chairs",
        "Internet connectivity issue"
    ],
    "Status": [
        "Pending",
        "Under Review",
        "Resolved",
        "Pending"
    ],
    "Assigned To": [
        "Faculty",
        "Department Head",
        "Maintenance",
        "IT Office"
    ]
})

st.dataframe(issues, use_container_width=True)

st.divider()

# ---------------------------------------------------
# STUDENT DIRECTORY
# ---------------------------------------------------
st.header("📇 Centralized Student Directory")

students = pd.DataFrame({
    "Name": [
        "Neil Caraig",
        "Adrian Espina",
        "Marisse De Vera",
        "Havena Balderama"
    ],
    "Email": [
        "neil@email.com",
        "adrian@email.com",
        "marisse@email.com",
        "havena@email.com"
    ],
    "Phone": [
        "09111111111",
        "09222222222",
        "09333333333",
        "09444444444"
    ]
})

st.dataframe(students, use_container_width=True)

st.divider()

# ---------------------------------------------------
# ANNOUNCEMENT SECTION
# ---------------------------------------------------
st.header("📢 Quick Announcement")

announcement = st.text_area(
    "Write announcement here"
)

if st.button("Post Announcement"):
    if announcement:
        st.success("Announcement posted successfully!")
    else:
        st.warning("Please type an announcement.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.divider()

st.caption("Scholastic Hub | Class Representative Dashboard")