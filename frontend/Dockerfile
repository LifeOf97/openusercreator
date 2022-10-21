####################
# Build vuejs app
####################
FROM node:18-buster-slim as BUILDER

# mark working directory
WORKDIR /app

# copy over dependency files and change owner
COPY package.json .

# install app dependencies
RUN npm install

# copy over the project and change owner
COPY . .

# build production ready app
RUN npm run build


###############################
# Final build
###############################
FROM node:18-buster-slim

# install production server
RUN npm install --global serve

ARG USER=realestkma

# create nonroot user/group
RUN useradd --create-home --shell /bin/bash --user-group $USER

# set user
USER $USER

# make directory to house app files/folders
RUN mkdir -p /home/$USER/app

# mark working directory
WORKDIR /home/$USER/app

# copy over dist folder from builder image
COPY --from=BUILDER --chown=$USER:$USER /app/dist ./dist