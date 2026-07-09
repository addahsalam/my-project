import os
import multiprocessing

bind = "0.0.0.0:8000"
backlog = 2048
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"
proc_name = "qr_attendance"
daemon = False
pidfile = "/var/run/gunicorn.pid"
