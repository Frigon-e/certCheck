FROM ubuntu:latest
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install net-tools nginx
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install python3.6
WORKDIR /usr/share/nginx/html 
COPY . .
EXPOSE 80 8080
CMD ["python3", "frontend.py"]

