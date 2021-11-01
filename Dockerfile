FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y git
RUN git clone https://gitlab.com/sjlawson/maxdata.git
RUN pip install --upgrade pip
WORKDIR /maxdata

RUN pip install -r requirements.txt

EXPOSE 8000
RUN python manage.py migrate
RUN python manage.py max_csv_import data_files/genre
RUN python manage.py max_csv_import data_files/artist
RUN python manage.py max_csv_import data_files/genre_artist

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]