# docker/Dockerfile
FROM ubuntu:22.04

# avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# install system dependencies + docker CLI
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    sshpass \
    slapd \
    ldap-utils \
    curl \
    git \
    build-essential \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# install python packages
RUN pip3 install --no-cache-dir \
    ansible==8.5.0 \
    requests===2.31.0 \
    webexteamssdk==1.6.1 \
    pyyaml==6.0.1 \
    python-ldap==3.4.3 \
    pytest==7.4.3

# create working directory
WORKDIR /automation

# copy project files
COPY ansible/ /automation/ansible/
COPY scripts/ /automation/scripts/

# set environment variables
ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/automation/scripts

# default command
CMD ["/bin/bash"]
