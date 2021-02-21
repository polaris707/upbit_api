FROM ubuntu:18.04

USER root

ARG DEBIAN_FRONTEND=noninteractive
RUN mkdir /home/project

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get install -y tzdata

# install python 3.9
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && \
    apt-get install -y python3.9 python3-pip && \
    apt-get install -y git

WORKDIR /home/project

RUN git clone https://github.com/polaris707/upbit_api upbit_api
