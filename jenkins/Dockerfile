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
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get install -y curl unzip && \
    curl -sLo allure.zip https://github.com/allure-framework/allure2/releases/download/2.33.0/allure-2.33.0.zip && \
    unzip -q allure.zip -d /usr/local/bin/allure && \
    rm allure.zip && \
    ln -s /usr/local/bin/allure/allure /usr/local/bin/allure

# Copy plugins.txt and install plugins
COPY plugin.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

USER jenkins