#!/bin/sh
project_name="mysite"

if [ ! -d $project_name ]; then
    django-admin startproject $project_name
fi

cd $project_name

nohup bash -c "python3 manage.py rqworker default 2>&1 &" 
python3 manage.py migrate && python3 manage.py runserver 0:8000
