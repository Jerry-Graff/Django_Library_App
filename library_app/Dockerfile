FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev \
    && apt-get clean

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "library_app.wsgi:application"]