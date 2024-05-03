import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd


# Sample data: replace with your actual data
data = pd.DataFrame({
    'name': ['Location1', 'Location2', 'Location3'],
    'lat': [34.0522, 36.7783, 40.7128],
    'lon': [-118.2437, -119.4179, -74.0060]
})

st.title('Map Selection App')

# Dropdown to select the location
option = st.sidebar.selectbox('Select a Location', data['name'])

# Finding the coordinates
lat = data[data['name'] == option]['lat'].values[0]
lon = data[data['name'] == option]['lon'].values[0]

# Create a map
m = folium.Map(location=[lat, lon], zoom_start=12)

# Add marker
folium.Marker([lat, lon], tooltip='Click for more', popup=option).add_to(m)

# Display the map
folium_static(m)
