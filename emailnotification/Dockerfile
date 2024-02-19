FROM python:3.10.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE emailnotification.settings

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]