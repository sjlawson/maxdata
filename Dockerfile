FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /maxdata
WORKDIR /maxdata
RUN pip install --upgrade pip
COPY requirements.txt /maxdata/

RUN pip install -r requirements.txt
COPY . /maxdata/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]