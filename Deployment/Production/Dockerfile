FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir app
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn
COPY . .
RUN "python manage.py migrate --noinput"
CMD ["gunicorn", "EverythingFlutter.wsgi", "-b", "0.0.0.0:8000"]