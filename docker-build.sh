#!/bin/sh

docker build -t docker-project_frontend:latest frontend/
docker tag docker-project_frontend:latest localhost:5000/docker-project_frontend:latest
docker build -t docker-project_api:latest api/
docker tag docker-project_api:latest localhost:5000/docker-project_api:latest
