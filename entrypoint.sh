#!/bin/bash


python manage.py runserver 0.0.0.0:8085 &
python consumer.py