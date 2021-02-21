FROM ubuntu:18.04

USER root

RUN mkdir /home/project

# install python 3.9
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && \
    apt-get install -y python3.9 python3-pip && \
    apt-get install -y git \
    apt-get clean

WORKDIR /home/project

RUN git clone https://github.com/polaris707/upbit_api upbit_api