import sqlite3
import streamlit as st
from datetime import datetime, timedelta,date

# Connect to the database
conn = sqlite3.connect('metadata_db/s3_metadata_goes.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to retrieve the year, day of the year, and hour of the day from the database
data = cursor.execute("SELECT Year, Day, Hour FROM goes;").fetchall()

# Close the connection
conn.close()

# Convert the year, day, and hour into a datetime object and store in a dict
dates_dict = {datetime(int(row[0]), 1, 1) + timedelta(int(row[1]) - 1, hours=int(row[2])): row for row in data}

# Create a set of unique dates
unique_dates = set(d.date() for d in dates_dict.keys())

# Create a date input widget
selected_date = st.date_input("Date:", min_value=min(unique_dates), max_value=max(unique_dates))

# Filter the hours for the selected date
hours = [datetime.time(d) for d in dates_dict.keys() if d.date() == selected_date]
hours_stripped = sorted(set(hours))

# Check if the selected date is in the database
if not hours_stripped:
    st.warning("No data found for the selected date.")
else:
    # Create a time input widget
    selected_time = st.selectbox("Hour", hours_stripped)

    # Combine the selected date and time into a single datetime object
    selected_datetime = datetime.combine(selected_date, selected_time)

    # Check if the selected datetime is in the database
    if selected_datetime not in dates_dict:
        st.warning("No data found for the selected date and time.")
    else:
        # Show the data for the selected datetime
        st.write(f"Data for selected date {selected_date} for the hour {selected_datetime.hour} is present on the metadata db")

