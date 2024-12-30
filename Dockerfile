# syntax=docker/dockerfile:1

# base python image for custom image
FROM python:3.9.13-slim-buster

# create working directory and install pip dependencies
WORKDIR /flask-coffee-wifi
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy python project files from local to /flask-coffee-wifi image working directory
COPY . .
ENV FLASK_APP=main.py

# run the flask server
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
