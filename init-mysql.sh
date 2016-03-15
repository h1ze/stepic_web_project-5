sudo /etc/init.d/mysql restart
mysql -u root -e "DROP DATABASE stepic_web_db;"
#create db in mysql
mysql -u root -e "CREATE DATABASE stepic_web_db;"
mysql -u root -e "CREATE USER 'stepic_web'@'localhost' IDENTIFIED BY 'stepic_web_pass';"
mysql -u root -e "GRANT ALL ON stepic_web_db.* TO 'stepic_web'@'localhost';"
#???
mysql -u root -e "FLUSH PRIVILEGES;"
python ./ask/manage.py syncdb
