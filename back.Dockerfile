FROM python:3.11-alpine

WORKDIR /app

COPY setup.py /app
COPY setup.cfg /app
COPY core /app/core
COPY web /app/web

RUN pip install .

EXPOSE 8000

ENTRYPOINT ["python", "web/api.py"]