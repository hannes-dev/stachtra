#!/bin/bash

if [ -f ".env" ]; then
    source .env
    python manage.py runserver
else
    echo "Please make an .env file based on .env_template and retry"
fi