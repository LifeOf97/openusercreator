import multiprocessing
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

bind = ["127.0.0.1:8000"]
# bind = "unix:/run/creator.sock"
workers = multiprocessing.cpu_count() * 2 + 1
reload_engine = "inotify"
group = "realestKMA"
user = "realestKMA"
reload = True

# logs
loglevel = "debug"
accesslog = F"{BASE_DIR}/logs/gunicorn/creator.access"
errorlog = F"{BASE_DIR}/logs/gunicorn/creator.error"
