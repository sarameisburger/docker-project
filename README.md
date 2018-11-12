# docker_project
test project for learning how to use docker

based on: https://github.com/highb/super-duper-meme

Components
frontend - The user-facing website
api - The backend API that powers the website, as well as integrators.
Setup
Use docker-compose build && docker-compose up to build and run.

If you want to do the builds manually:

pushd api; docker build -t super-duper-meme_api .; popd
pushd frontend; docker build -t super-duper-meme_frontend .; popd
