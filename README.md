# MAX Artist / Genre data sample project

name: `maxdata`
repository location: `https://gitlab.com/sjlawson/maxdata.git`

## Description:
This is a fully functional Django application. The goal is to demonstrate parsing CSV files of specific format to be imported into different database tables, and then to execute queries that show a handful of relationships between the data. 
  - Project was built with Python3.9 and Sqlite3 -- could be easily modified for any SQL database
  - The data and query examples are viewable without logging into the admin interface
  - The manager utility to import is also usable without admin authentication; can be used as an import utility
  - When running, potentially useful SQL queries have been built-in to several Django views available from the applications main navigation menu


## Installation with Docker
1. Run `docker build -t maxdata https://gitlab.com/sjlawson/maxdata.git#master`
2. Run contatiner: `docker run -p 8000:8000 maxdata`
3. Explore data by directing a web browser to `http://0.0.0.0:8000/`


## Installation on a host environment
1. clone the repository and `cd maxdata`
2. create a python virtual environment e.g. `python3.9 -m venv venv` and run `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. import the sample data:
  - `python manage.py max_csv_import data_files/genre`
  - `python manage.py max_csv_import data_files/artist`
  - `python manage.py max_csv_import data_files/genre_artist`
6. run the server with: `python manage.py runserver`
7. Explore data by directing a web browser to `http://0.0.0.0:8000/`


## General usage for data import
When the project has been setup on a host system, other data files may be imported with the `max_csv_import` manager command mentioned in step *5* above.
