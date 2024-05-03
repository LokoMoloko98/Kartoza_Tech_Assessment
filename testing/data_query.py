import sqlite3
import pandas as pd
import json

# Connect to SQLite database
conn = sqlite3.connect('CT-TSMs.db')
query = """
SELECT PNT, geometry FROM town_survey_marks
"""
data = pd.read_sql(query, conn)
conn.close()

# Parse the geometry data to extract coordinates
data['coordinates'] = data['geometry']

print(json.loads(data["coordinates"].values[0])["coordinates"][1])