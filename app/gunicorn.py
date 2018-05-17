"""gunicorn WSGI server configuration."""

from multiprocessing import cpu_count

max_requests = 1000
workers = cpu_count() * 2 + 1
