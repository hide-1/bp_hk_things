FROM ubuntu:22.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    git \
    ssh \
    curl \
    net-tools \
    iputils-ping \
    python3.10


WORKDIR /root/workdir
