sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx start
sudo ln -s /home/box/web/etc/gunicorn.py  /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
cd /home/box/web/
sudo gunicorn -c /home/box/web/etc/gunicorn.py hello:application
