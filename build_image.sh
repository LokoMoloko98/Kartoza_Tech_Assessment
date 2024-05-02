#!/bin/bash

# Run the docker build command
docker build -t ngx_test_container --build-arg HOST_NAME=$HOSTNAME .
docker run -e CONTAINER_IP=$(hostname -i) --name mynginx1 -p 80:80 -d ngx_test_container
