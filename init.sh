#!/usr/bin/env bash
# ini file for work

# При входе в терминал надо запустить Ngnix и проверить:
sudo /etc/init.d/nginx start
# ps -o pid,euser,egroup,comm,args -C nginx

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn_conf.py   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_conf_ask.py /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

