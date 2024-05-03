#Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Convert the CT TSM geojson file into a table in an SQLite database file
RUN geojson-to-sqlite CT-TSMs.db town_survey_marks Town_Survey_Marks_1000.geojson 

# Make port 8501 available to the world outside this container
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run TSM_browser.py when the container launches
ENTRYPOINT ["streamlit", "run", "TSM_browser.py", "--server.port", "8501", "--server.address", "0.0.0.0", "--server.enableCORS", "false", "--server.enableWebsocketCompression=false"]