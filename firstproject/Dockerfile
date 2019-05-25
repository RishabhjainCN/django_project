FROM python:3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install sqlite3
RUN mkdir /firstproject
EXPOSE 8000
EXPOSE 8080
WORKDIR /firstproject
COPY requirements.txt /firstproject/
RUN pip install -r requirements.txt
COPY python-flask-server/requirements.txt /firstproject/
RUN pip install -r requirements.txt
COPY . /firstproject/
RUN chmod u+x Entrypoint.sh
CMD sh Entrypoint.sh