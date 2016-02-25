# -*- coding: utf-8 -*-

import os
# import sys
# import inspect

# BASE_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# sys.path.append(BASE_DIR)

# Server Socket
bind = '{:s}:{:d}'.format('0.0.0.0', 8080)

# Worker Processes
workers = 1
worker_class = 'sync'
threads = 1

# Debugging
reload = False
check_config = False

# Server Mechanics
# chdir = BASE_DIR
# daemon = True
# pidfile = os.path.join(BASE_DIR, 'tmp', 'pid', '{:s}.pid'.format(conf.SERVICE_NAME))

# Logging
# accesslog = os.path.join(BASE_DIR, 'logs', 'access.log')
# errorlog = os.path.join(BASE_DIR, 'logs', 'error.log')
# loglevel = conf.LOG_LEVEL
