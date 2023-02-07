import sqlite3
import streamlit as st
from datetime import datetime, timedelta,time,date
import goes_module as goes_module

# Connect to the database
conn = sqlite3.connect('../metadata_db/s3_metadata_goes.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to retrieve the year, day of the year, and hour of the day from the database
cursor.execute("SELECT Year, Day, Hour FROM goes;")

# Fetch all the results of the query
data = cursor.fetchall()

# Close the connection
conn.close()

# Convert the year, day, and hour into a datetime object
dates = [datetime(int(row[0]), 1, 1) + timedelta(int(row[1]) - 1, hours=int(row[2])) for row in data]


file_to_download = ''
dest_url = ''

with st.form(key="my_form"):
    st.title("GOES")
    selected_date = st.date_input("Date:", min_value=min(dates), max_value=date.today())
    selected_time = st.time_input("Time:")

    year = selected_date.strftime("%Y")
    month = selected_date.strftime("%m")
    day = selected_date.strftime("%d")
    hour = selected_time.strftime("%H")

    search_fields = st.form_submit_button(label="Search")

    recommended_files = goes_module.get_files_goes(year, month, day, hour)
    selected_files = goes_module.get_files_goes(year, month, day, hour)
    file_to_download = st.selectbox("Please select file for download: ",selected_files)
    download = st.form_submit_button("download")

    if download:
        dest_url = goes_module.copy_to_s3(file_to_download, "noaa-goes18", "goes-team6")
        st.write(dest_url)

