FROM jenkins/jenkins:latest-jdk17
USER root
RUN apt-get update && apt-get install -y lsb-release sudo

# Install required packages in a single layer to minimize image size
RUN apt-get update && apt-get install -y \
    lsb-release \
    sudo \
    curl \
    unzip \
    python3 \
    python3-pip \
    python3.11-venv \
    allure \

    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy plugins.txt and install plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

USER jenkins