import sqlite3
import streamlit as st
from datetime import datetime, timedelta,time,date
import goes_module as goes_module


st.set_page_config(page_title="GOES", page_icon=":satellite:", layout="wide")
# Connect to the database
conn = sqlite3.connect('metadata_db/s3_metadata_goes.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to retrieve the year, day of the year, and hour of the day from the database
cursor.execute("SELECT Year, Day, Hour FROM goes;")

# Fetch all the results of the query
data = cursor.fetchall()

# Close the connection
conn.close()

# Convert the year, day, and hour into a datetime object and store in a dict
dates_dict = {datetime(int(row[0]), 1, 1) + timedelta(int(row[1]) - 1, hours=int(row[2])): row for row in data}

# Create a set of unique dates
unique_dates = set(d.date() for d in dates_dict.keys())

file_to_download = ''
dest_url = ''

with st.form(key="my_form"):
    st.title("GOES")
    # Create a date input widget
    selected_date = st.date_input("Date:", min_value=min(unique_dates), max_value=date.today())
    # selected_time = st.time_input("Time:")
    if selected_date:
        submit_button = st.form_submit_button("Next")
    hours = [datetime.time(d) for d in dates_dict.keys() if d.date() == selected_date]
    hours_stripped = sorted(set(hours))

    # Check if the selected date is in the database
    if not hours_stripped:
        st.warning("No data found for the selected date.")
    else:
        # Create a time input widget
        hours_stripped.insert(0,'Select')
        selected_time = 'Select'
        selected_time = st.selectbox("Hour:", hours_stripped)

        search_fields = st.form_submit_button(label="Search")
        # Combine the selected date and time into a single datetime object
        if type(selected_time) == str:
            pass
        else:
            selected_datetime = datetime.combine(selected_date, selected_time)
            year = selected_date.strftime("%Y")
            month = selected_date.strftime("%m")
            day = selected_date.strftime("%d")
            hour = selected_time.strftime("%H")

            recommended_files = goes_module.get_files_goes(year, month, day, hour)
            st.write('Number of files found:',len(recommended_files))
            selected_files = goes_module.get_files_goes(year, month, day, hour)
            # if search_fields:
            file_to_download = st.selectbox("Please select file for download: ",selected_files)
            download = st.form_submit_button("Download")
            if download:
                dest_url = goes_module.copy_to_s3(file_to_download, "noaa-goes18", "goes-team6")
                st.write(dest_url)

            # Check if the selected datetime is in the database
            if selected_datetime not in dates_dict:
                st.warning("No data found for the selected date and time.")
            else:
                # Show the data for the selected datetime
                st.write("Data for selected date and hour is present on the metadata db",selected_date, selected_datetime.hour)

