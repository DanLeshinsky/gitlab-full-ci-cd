FROM python:3.10-alpine3.19

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.3.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.3/allure-commandline-2.13.3.tgz && \
    tar -zxvf allure-2.13.3.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.3/bin/allure /usr/bin/allure && \
    rm allure-2.13.3.tgz

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install -r requirements.txt