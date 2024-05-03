import streamlit as st
import sqlite3
import folium
from streamlit_folium import folium_static
import pandas as pd
import json

st.set_page_config(
    page_title="Cape Town TSM Browser",
    page_icon="🗺️", 
    layout="wide",  
    initial_sidebar_state="expanded"
)

# Styling
st.markdown("""
<style>
.main {
    background-color: #F0F2F6;
}
h1 {
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# Connect to SQLite database
conn = sqlite3.connect('CT-TSMs.db')
query = """
SELECT PNT, geometry FROM town_survey_marks
"""
data = pd.read_sql(query, conn)
conn.close()

# Parse the geometry data to extract coordinates
data['coordinates'] = data['geometry']

# Title of the dashboard
st.title('City of Cape Town')
st.header('Town Survey Mark (TSM) Browser Web App', divider="blue")
st.markdown("""
### Simple TSM Browser Web App Overview
This TSM Browser Web App provides an interactive platform for users to explore Town Survey Marks (TSM) within the City of Cape Town. 
Users can select a TSM from a dropdown menu or if they know the TSM ID, they can search for it, and the app will automatically zoom 
in on the map to display the location
""")


# Dropdown to select the location
option = st.sidebar.selectbox('Select a Town Survey Mark', data['PNT'])

# Finding the coordinates
selected_mark = data[data['PNT'] == option]
# lat = selected_mark['coordinates'].apply(lambda x: x[1]).values[0]  # Latitude 
# lon = selected_mark['coordinates'].apply(lambda x: x[0]).values[0]  # Longitude 

lat = json.loads(selected_mark["coordinates"].values[0])["coordinates"][1]
lon = json.loads(selected_mark["coordinates"].values[0])["coordinates"][0]

# Create a map
m = folium.Map(location=[lat, lon], zoom_start=12)

# Add marker
folium.Marker([lat, lon], tooltip='Click for more', popup=option).add_to(m)

# Display the map
folium_static(m)
