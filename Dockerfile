# Use the latest version of the Amazon Linux base image
FROM ubuntu

# Update all installed packages to thier latest versions
RUN apt-get update

# Install the unzip package, which we will use it to extract the web files from the zip folder
RUN apt-get install nginx -y

# Change directory to the html directory
WORKDIR /var/www/html

# Install Git
RUN apt-get install -y git 

ENV CONTAINER_IP=$CONTAINER_IP

# Copy the web files into the HTML directory
COPY index.html /var/www/html
COPY script.js /var/www/html
COPY style.css /var/www/html
COPY images/'Moloko_logo.png' /var/www/html

#Replace line 58 with correct line
RUN sed -i '57i <p class="p404" data-depth="0.50">The container is successfully deployed.</p>' /var/www/html/index.html

# Expose the default Nginx ports
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
