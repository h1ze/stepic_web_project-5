
# Apache
unlink /etc/nginx/sites-enabled/default

ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/stepic_webtech.conf

# Gunicorn
ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py