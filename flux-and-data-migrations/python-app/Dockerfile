FROM python:3.9


WORKDIR /code/app

RUN mkdir -p /data
RUN apt update && apt install sqlite3 -y && apt clean

COPY ./flux-and-data-migrations/python-app/requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./flux-and-data-migrations/python-app /code/app


CMD ["fastapi", "run", "main.py", "--port", "8000"]