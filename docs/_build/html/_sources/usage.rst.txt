Usage
=====

Once you have installed MyTennisClub, you can start using by running the following command :
`python3 manage.py runserver`

This will start the Django development server and you can access the app on the browser by following the address `http://127.0.0.1:8000/`

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~
Here are some management commands

- `python3 manage.py migrate` - Apply database migrations.
- `python3 manage.py createsuperuser` - Create an admin user for the project

Configuration
~~~~~~~~~~~~~

The project comes with several configurable settings that you can customize by modifying the `settings.py` file. You can adjust the following settings:

- `DATABASES`: Configure your database connection.
- `INSTALLED_APPS`: Add or remove Django apps.
- `ALLOWED_HOSTS`: List of allowed hosts for your Django project.