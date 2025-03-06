FROM python:3.11.10-alpine3.20

WORKDIR /usr/src

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

ENV DATABASE_URL ${DATABASE_URL}
COPY ./app ./app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]