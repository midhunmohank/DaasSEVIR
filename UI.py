import streamlit as st
import datetime
import pandas as pd
# import folium

st.title("GOES")
st.date_input("Date: ")

state_codes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
               'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
               'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
               'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
               'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

cities = {
    'AL': ['Birmingham', 'Montgomery', 'Mobile', 'Huntsville'],
    'AK': ['Anchorage', 'Fairbanks', 'Juneau'],
    'AZ': ['Phoenix', 'Tucson', 'Mesa', 'Chandler'],
    'AR': ['Little Rock', 'Fort Smith', 'Fayetteville'],
    'CA': ['Los Angeles', 'San Diego', 'San Francisco', 'San Jose'],
    'CO': ['Denver', 'Colorado Springs', 'Aurora'],
    'CT': ['Bridgeport', 'New Haven', 'Hartford'],
    'DE': ['Wilmington', 'Dover'],
    'FL': ['Jacksonville', 'Miami', 'Tampa', 'Orlando'],
    'GA': ['Atlanta', 'Augusta', 'Columbus'],
    'HI': ['Honolulu', 'Hilo'],
    'ID': ['Boise', 'Nampa', 'Idaho Falls'],
    'IL': ['Chicago', 'Aurora', 'Rockford'],
    'IN': ['Indianapolis', 'Fort Wayne', 'Evansville'],
    'IA': ['Des Moines', 'Cedar Rapids', 'Davenport'],
    'KS': ['Wichita', 'Overland Park', 'Kansas City'],
    'KY': ['Louisville', 'Lexington', 'Bowling Green'],
    'LA': ['New Orleans', 'Baton Rouge', 'Shreveport'],
    'ME': ['Portland', 'Lewiston', 'Bangor'],
    'MD': ['Baltimore', 'Frederick', 'Rockville'],
    'MA': ['Boston', 'Worcester', 'Springfield'],
    'MI': ['Detroit', 'Grand Rapids', 'Warren'],
    'MN': ['Minneapolis', 'Saint Paul', 'Rochester'],
    'MS': ['Jackson', 'Gulfport', 'Southaven'],
    'MO': ['Kansas City', 'Saint Louis', 'Springfield'],
    'MT': ['Billings', 'Missoula', 'Great Falls'],
    'NE': ['Omaha', 'Lincoln', 'Bellevue'],
    'NV': ['Las Vegas', 'Reno', 'Henderson'],
    'NH': ['Manchester', 'Nashua', 'Concord'],
    'NJ': ['Newark', 'Jersey City', 'Paterson'],
    'NM': ['Albuquerque', 'Las Cruces', 'Rio Rancho'],
    'NY': ['New York', 'Buffalo', 'Rochester', 'Yonkers'],
    'NC': ['Charlotte', 'Raleigh', 'Greensboro'],
    'ND': ['Fargo', 'Bismarck', 'Grand Forks'],
    'OH': ['Columbus', 'Cleveland', 'Cincinnati'],
    'OK': ['Oklahoma City', 'Tulsa', 'Norman'],
    'OR': ['Portland', 'Eugene', 'Salem'],
    'PA': ['Philadelphia', 'Pittsburgh', 'Allentown'],
    'RI': ['Providence', 'Warwick', 'Cranston'],
    'SC': ['Columbia', 'Charleston', 'North Charleston'],
    'SD': ['Sioux Falls', 'Rapid City', 'Aberdeen'],
    'TN': ['Nashville', 'Memphis', 'Knoxville'],
    'TX': ['Houston', 'San Antonio', 'Dallas', 'Austin'],
    'UT': ['Salt Lake City', 'West Valley City', 'Provo'],
    'VT': ['Burlington', 'Essex', 'South Burlington'],
    'VA': ['Virginia Beach', 'Norfolk', 'Chesapeake'],
    'WA': ['Seattle', 'Spokane', 'Tacoma'],
    'WV': ['Charleston', 'Huntington', 'Parkersburg'],
    'WI': ['Milwaukee', 'Madison', 'Green Bay'],
    'WY': ['Cheyenne', 'Casper', 'Laramie']
}

selected_state = st.selectbox("Select a state", state_codes)
selected_cities = st.multiselect("Select one or more cities", cities[selected_state])
st.write("You selected: ", selected_cities)

button_search = st.button("Search")
if button_search:
    random = ['A', 'B', 'C']
    select_file = st.selectbox("Select a file: ", random)
    print(select_file)

# download = st.download_button("Download", select_file)
# if download:
#     st.write(select_file)

df = pd.read_excel("files/Book.xlsx")

st.title("Map Visualization using Streamlit")

st.write("Average Latitude: ", df['LAT'].mean())
st.write("Average Longitude: ", df['LON'].mean())

df['text'] = df['NAME']

st.map(df, zoom=5, markers={"text": (df['LAT'], df['LON'])})

st.map(df, zoom=5, center=(df['LAT'].mean(), df['LON'].mean()), markers={"text": (df['LAT'], df['LON'])})

# import streamlit as st
# import pandas as pd

# data = {'ICAO': ['KABR', 'KABX', 'KAKQ', 'KAMA'],
#         'LAT': [45.455833, 35.149722, 36.98405, 35.233333],
#         'LON': [-98.413333, -106.82388, -77.007361, -101.70927]}
# df = pd.DataFrame(data)

# st.title("Map Visualization using Streamlit")

# st.write("Average Latitude: ", df['LAT'].mean())
# st.write("Average Longitude: ", df['LON'].mean())

# st.map(df, zoom=5)