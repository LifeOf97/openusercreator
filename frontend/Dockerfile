####################
# Build vuejs3 app
####################
FROM node:18-buster-slim as builder


ARG USER=realestkma

# create nonroot user/group
RUN useradd --create-home --shell /bin/bash --user-group $USER

# set user
USER $USER

# make directory to house app files/folders
RUN mkdir -p /home/$USER/app

# mark working directory
WORKDIR /home/$USER/app

# copy over dependency files and change owner
COPY --chown=$USER:$USER package.json .
COPY --chown=$USER:$USER package-lock.json .

# install app dependencies
RUN npm install

# copy overe the project and change owner
COPY --chown=$USER:$USER . .

# build production ready app
RUN npm run build