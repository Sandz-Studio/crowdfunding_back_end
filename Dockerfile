ARG PYTHON_VERSION=3.12-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

RUN ls -la /path/to/your/static/directory/
RUN python manage.py collectstatic --noinput

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY crowdfunding/ /code/

ENV SECRET_KEY "y4nROk6AduAFJljCdKf1U4rnWIqDs7AUYqE16XB4Us6WHbjL9V"
RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "crowdfunding.wsgi"]
CMD ["/code/run.sh"]