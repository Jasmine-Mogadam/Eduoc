FROM python:3.10-slim

WORKDIR /app

#If we add the requirements and install dependencies first, docker can use cache if requirements don't change
COPY requirements.txt /app

RUN pip install -r requirements.txt --user

COPY . /app
CMD python server.py

EXPOSE 3000
