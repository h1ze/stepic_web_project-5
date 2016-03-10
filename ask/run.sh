#!/bin/bash
gunicorn -c /etc/gunicorn.d/gunicorn.conf ask.wsgi
