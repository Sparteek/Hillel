FROM jenkins/jenkins:lts-jdk17

USER root

# Python потрібен Jenkins для створення venv та запуску pytest.
RUN apt-get update \
    && apt-get install --yes --no-install-recommends python3 python3-pip python3-venv git \
    && rm -rf /var/lib/apt/lists/*

USER jenkins

# Плагіни для pipeline, GitHub, результатів тестів, Allure та поштових сповіщень.
RUN jenkins-plugin-cli --plugins \
    workflow-aggregator \
    pipeline-stage-view \
    git \
    github \
    junit \
    allure-jenkins-plugin \
    email-ext \
    credentials-binding \
    timestamper
