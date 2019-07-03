FROM ubuntu:latest
LABEL maintainer="vreddy575757@gmail.com"

RUN apt-get update
RUN apt-get install python python-pip python3 -y
RUN pip install requests
ADD ./getVendor.py /root
USER root
WORKDIR /root
CMD ["/bin/bash"]
