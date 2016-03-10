#!/bin/bash
sudo /bin/ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/gunicorn.conf
