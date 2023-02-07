# # import streamlit as st
# # import pandas as pd
# # import numpy as np

# # st.title('UBER PICKUPS IN NYC')

# # DATE_COLUMN = 'date/time'
# # DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
# #          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# # def load_data(nrows):
# #     data = pd.read_csv(DATA_URL, nrows=nrows)
# #     lowercase = lambda x: str(x).lower()
# #     data.rename(lowercase, axis='columns', inplace=True)
# #     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
# #     return data

# # # Create a text element and let the reader know the data is loading.
# # data_load_state = st.text('Loading data...')
# # # Load 10,000 rows of data into the dataframe.
# # with st.spinner('Wait for it...'):
# #     data = load_data(10000)
# # # Notify the reader that the data was successfully loaded.
# # data_load_state.text('Loading data...done!')

# # st.subheader('Raw data')
# # st.write(data)

# # st.subheader('Number of pickups by hour')

# # hist_values = np.histogram(
# #     data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# # st.bar_chart(hist_values)

# # st.subheader('Map of all pickups')
# # st.map(data)

# # st.subheader('Map of all pickups')
# # st.map(data)
# # ### PLOTLY TO CREATE INTERACTIVE GRAPHS

# # ##BUTTON
# # # if st.button('Say hello'):
# # #     st.write('Why hello there')
# # # else:
# # #     st.write('Goodbye')

# # ### RADIO, DROPDOWN, SLIDERS, FILE INPUT, TIME, CAMERA
# # ## LAYOUT AND CONTAINERS
# # ## STATUS ELEMENTS
# # ##spinny while loading


# import streamlit as st

# # Data for different sports teams
# teams = {
#     "baseball": {"team": "New York Yankees", "wins": 103, "losses": 59},
#     "basketball": {"team": "Los Angeles Lakers", "wins": 36, "losses": 7},
#     "football": {"team": "Kansas City Chiefs", "wins": 14, "losses": 2},
#     "hockey": {"team": "Tampa Bay Lightning", "wins": 36, "losses": 10},
# }

# # Create a function that displays information about a selected team
# def show_team_info(team_name):
#     team_info = teams[team_name]
#     st.write(f"Team: {team_info['team']}")
#     st.write(f"Wins: {team_info['wins']}")
#     st.write(f"Losses: {team_info['losses']}")

# # Create a dropdown menu to select a team
# team_name = st.selectbox("Select a team", list(teams.keys()))

# # Show the selected team's information
# show_team_info(team_name)



import streamlit as st
import datetime
import pandas as pd

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
    selected_file = st.selectbox("Select a file: ", random)
    print(selected_file)

download = st.button("Download")
if download:
    print(selected_file)