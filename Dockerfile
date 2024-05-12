FROM python:3.11-alpine

WORKDIR /app

COPY core /app/core
COPY web /app/web
COPY setup.py /app
COPY setup.cfg /app

RUN pip install .

ENTRYPOINT ["python", "web/api.py"]