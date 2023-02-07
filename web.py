
import streamlit as st
import pandas as pd
import folium

# Load the latitude and longitude data into a pandas dataframe
data = {'ICAO': ['KABR', 'KABX', 'KAKQ', 'KAMA'],
        'LAT': [45.455833, 35.149722, 36.98405, 35.233333],
        'LON': [-98.413333, -106.82388, -77.007361, -101.70927]}
df = pd.DataFrame(data)

st.title("Map Visualization using Streamlit")

# Create the map using folium and display in Streamlit
map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=5)

for lat, lon, name in zip(df['LAT'], df['LON'], df['ICAO']):
    folium.Marker(location=[lat, lon], popup=name).add_to(map)

st.write(map)