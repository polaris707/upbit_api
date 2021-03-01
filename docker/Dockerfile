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
    apt-get install -y python3.9 python3.9-distutils && \
    apt-get install -y git curl

ENV PYTHONIOENCODING=utf-8

# pip install
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.9 get-pip.py

COPY requirements.txt /temp/requirements.txt
RUN pip3.9 install -r /temp/requirements.txt

# set alias
RUN echo 'alias python="python3.9"' >> ~/.bashrc
RUN echo 'alias pip="pip3.9"' >> ~/.bashrc

WORKDIR /home/project

RUN git clone https://github.com/polaris707/upbit_api upbit_api
