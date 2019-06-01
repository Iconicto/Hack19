FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir app
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["python", "manage.py", "migrate", "--noinput"]
