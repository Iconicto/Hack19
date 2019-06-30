FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir app
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn
COPY . .
CMD 'bash -c "python manage.py migrate --noinput && gunicorn EverythingFlutter.wsgi -b 0.0.0.0:8000"'