#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default

cd ..
sudo ln -s etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

gunicorn -c etc/gunicorn_conf.py hello:application &

cd ask
gunicorn -c ../etc/gunicorn_django_conf.py ask.wsgi --pythonpath '/home/box/web/ask' &