########################
# BUILDER
########################
FROM python:3.10-slim-buster as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


########################
# FINAL IMAGE
########################
FROM python:3.10-slim-buster

# install deps
RUN apt update && apt-get -y install netcat

ARG USER=realestkma

# create nonroot user/group
RUN useradd --create-home --shell /bin/bash --user-group $USER

# update/upgrade pip
RUN pip install --upgrade pip

# activate system user
USER $USER

# create needed directories
ENV HOME=/home/$USER
ENV APP_HOME=$HOME/app
RUN mkdir $APP_HOME
RUN mkdir -p $APP_HOME/logs/gunicorn
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# copy over required dependencies
COPY --from=builder --chown=$USER:$USER /app/wheels /wheels
COPY --from=builder --chown=$USER:$USER /app/requirements.txt .

# add required dir to PATH, to fix python path not in PATH error
ENV PATH="${PATH}:${HOME}/.local/bin"

# install dependencies
RUN pip install --user --no-cache /wheels/*

# copy over entrypoint.sh and mark it as executable
COPY --chown=$USER:$USER ./entrypoint.sh .
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project over
COPY --chown=$USER:$USER . .

ENTRYPOINT [ "/home/realestkma/app/entrypoint.sh" ]