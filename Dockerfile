FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY app /app
RUN pip install Flask \
    && pip install APScheduler \
    && pip install -U flask-cors \
    && pip install wikipedia