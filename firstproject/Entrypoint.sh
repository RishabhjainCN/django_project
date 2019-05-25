#!/bin/bash
python manage.py runserver 0.0.0.0:8000 &
cd python-flask-server
python3 -m swagger_server 0.0.0.0:8080
