#!/bin/bash
sudo service mysql start
mysql -uroot -e "CREATE USER 'mysql_user'@'localhost' IDENTIFIED BY 'Qa4kT2e4XC'"
mysql -umysql_user -pQa4kT2e4XC -e "create database django_ask"
mysql -umysql_user -pQa4kT2e4XC -e "GRANT ALL PRIVILEGES ON * . * TO 'mysql_user'@'localhost'"
mysql -umysql_user -pQa4kT2e4XC -e "FLUSH PRIVILEGES;"

python manage.py syncdb