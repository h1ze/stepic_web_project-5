sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn-django.conf   /etc/gunicorn.d/stepic-web-django
sudo /etc/init.d/gunicorn restart

sudo sed -i 's/skip-external-locking/skip-external-locking\ninnodb_use_native_aio = 0/' /etc/mysql/my.cnf
sudo /etc/init.d/mysql start  
sudo mysql -uroot -e "create database stepic_web_db CHARACTER SET utf8 COLLATE utf8_general_ci;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web_db.* TO 'stepic_web'@'localhost' IDENTIFIED BY 'stepic_web_pass';"
mysql -u root -e "FLUSH PRIVILEGES;"
sudo pip install django-autofixture
sudo python /home/box/web/ask/manage.py syncdb
sudo python /home/box/web/ask/manage.py loadtestdata qa.Question:40
sudo python /home/box/web/ask/manage.py loadtestdata qa.Answer:40


