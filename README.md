# MAX Artist / Genre data sample project

name: `maxdata`
repository location: `https://gitlab.com/sjlawson/maxdata.git`

## Description:
This is a fully functional Django application.
  - Project was build with Python3.9 and Sqlite3
  - The data and query examples are viewable without logging into the admin interface.
  - The manager utility to import is also usable without admin authentication; will run as a utility
  - When running, potentially useful SQL queries have been built-in to several Django views available from the applications main navigation menu


## Installation with Docker
1. Download the `Dockerfile` from the above repository (or clone the repository)
2. Build container from the directory containing the Dockerfile: `docker build -t maxdata .`
3. Run contatiner: `docker run -p 8000:8000 maxdata`
4. Explore data by directing a web browser to `http://0.0.0.0:8000/`


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
