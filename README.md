# Kartoza Technical Assessment 

Moloko Mokubedi's Kartoza technical assessment submission. This submission demonstrates a simple orchestration of a simple Town Survey Mark (TSM) Browser Web App using Docker-Compose and Traefik.

## About the Web App
The Web-App is a Streamlit Dashboard that is connected to an SQLite Database that holds a subset of the records of the Town Survey Marks situated in the Cape Town region. (The Data is courtsy of the [City of Cape Town's Open Data Portal](https://odp-cctegis.opendata.arcgis.com/datasets/4ee4fef293d74436afe31c2b979dfb30_14/about).) The web app makes it possible for user to select a TSM from a dropdown menu or if they know the TSM ID, they can search for it, and the app will automatically zoom 
in on the map to display it's location. 

## Services
This Docker Compose setup deploys a the web app behind a Traefik reverse proxy that handles HTTPS requests using SSL certificates managed by Let's Encrypt.

 1. ```reverse-proxy``` (Traefik): Handles HTTPS requests and automatically issues and renews SSL certificates via Let's Encrypt.
 
 2. ```tsm-browser-app``` (tsm-browser-app): The Simple TSM Browser Web App

## Usage
### 1. Clone the Repository:
```
git clone https://github.com/LokoMoloko98/Kartoza_Tech_Assessment.git
```

### 2. Navigate to the Project Directory:
```
cd /Kartoza_Tech_Assessment
```

### 3. Create a .env file with your fully qualified domain name (FQDN):
```
echo "fqdn=<root level domain>" > .env
```

### 4. Launch the Application:
```
docker-compose --env-file .env up -d
```

## Deployment Workflow
1. Docker Compose reads the configuration, then builds and eventually starts the services defined.
2. Traefik sets up routing, SSL configuration, and starts listening for incoming requests on port 443.
3. SSL Certificates are requested by Traefik from Let's Encrypt for the configured domain name, ensuring HTTPS traffic is securely encrypted.
4. Health Checks ensure continuous monitoring and readiness of the services for handling web traffic.


## SSL Certificates
- The SSL certificate generation by Let's Encrypt is triggered when the reverse-proxy service starts, given that the host (${fqdn}) is properly set to a fully qualified domain name (FQDN) that resolves to the public IP of the machine hosting the docker container.

- Locally: The SSL certificate is not valid when deployed locally because Let's Encrypt cannot verify a domain name mapped to a local development environment. It requires that the domain be publicly accessible on the internet for domain verification.

## Health Checks
- Dockerfile: A health check for the web-app container has been set up in in the Dockerfile to automatically check the health of the container. The health check makes a curl request internally so see if the Streamlit app is still accessible via ists local access url.

- Traefik Dashboard: Provides real-time monitoring of the router's health and other metrics. This feature is accessible on port 8080 and is enabled for the container running Traefik.
