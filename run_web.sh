#!/bin/sh
project_name="mysite"

if [ ! -d $project_name ]; then
    django-admin startproject $project_name
fi

cd $project_name

nohup bash -c "sleep 10 && python3 manage.py rqworker default 2>&1 &" 
nohup bash -c "sleep 10 && python3 manage.py migrate && python3 manage.py runserver 0:8000 2>&1 &"
uwsgi --http :8000 --module mysite.wsgi
