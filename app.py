import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# File for storing task data
FILE_NAME = "nursing_tasks.csv"

# Initialize CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Task Name", "Category", "Time Spent (minutes)"])
    df.to_csv(FILE_NAME, index=False)

# Load existing data from the CSV file
df = pd.read_csv(FILE_NAME)

# Title of the app
st.title("Nursing Task Tracker")

# Form for adding a new task
with st.form("task_form"):
    task_name = st.text_input("Task Name")
    category = st.selectbox("Category", ["Medications", "Patient Care", "Documentation", "Other"])
    time_spent = st.number_input("Time Spent (minutes)", min_value=1, step=1)
    submitted = st.form_submit_button("Add Task")

# When form is submitted, add the task to the CSV
if submitted and task_name:
    new_task = pd.DataFrame([[task_name, category, time_spent]], columns=["Task Name", "Category", "Time Spent (minutes)"])
    df = pd.concat([df, new_task], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)  # Save to CSV
    st.success(f"Added task: {task_name}")

# Display tasks with delete buttons
st.header("Logged Tasks")
st.dataframe(df)

# Delete tasks when the delete button is pressed
for index, row in df.iterrows():
    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])  # Layout for better alignment
    col1.write(f"**{row['Task Name']}**")
    col2.write(f"{row['Time Spent (minutes)']} min")
    col3.write(f"**{row['Category']}**")
    if col4.button("❌", key=f"delete_{index}"):
        df = df.drop(index)
        df = df.reset_index(drop=True)
        df.to_csv(FILE_NAME, index=False)  # Update CSV after deletion
        st.success(f"Deleted task: {row['Task Name']}")
        st.rerun()  # Refresh the app to update UI

# Visualization of time spent on tasks by category
if not df.empty:
    st.subheader("Time Spent on Tasks by Category")
    
    # Aggregate time spent by category
    category_time = df.groupby("Category")["Time Spent (minutes)"].sum()
    
    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(category_time, labels=category_time.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Show the pie chart
    st.pyplot(fig)

# Visualization for time spent on tasks by category
if not df.empty:
    st.subheader("Time Spent by Category")
    
    # Group the tasks by category and sum the time spent
    time_by_category = df.groupby('Category')['Time Spent (minutes)'].sum().sort_values()

    # Create a bar chart
    fig, ax = plt.subplots()
    time_by_category.plot(kind='barh', ax=ax, color='skyblue')
    ax.set_xlabel("Time Spent (minutes)")
    ax.set_ylabel("Task Category")
    ax.set_title("Total Time Spent by Task Category")

    # Display the chart
    st.pyplot(fig)
