FROM ubuntu:jammy

# Install dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common

# Install Cmake
RUN apt-get install -y cmake
RUN apt-get install -y sudo
RUN apt-get install -y wget
RUN apt-get install -y gcc build-essential

ENV USER_NAME=user
# Create User
RUN useradd -ms /bin/bash $USER_NAME
RUN echo "$USER_NAME:$USER_NAME" | chpasswd && adduser $USER_NAME sudo
RUN echo "$USER_NAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER $USER_NAME

# Set working directory
WORKDIR /home/$USER_NAME

# Copy the source code
VOLUME /home/$USER_NAME
RUN mkdir -p /home/$USER_NAME/build
