# Django DCN

Django DCN is a website used to create, view, and change DCN's for use in production environments.

## Installation

1. Start by installing Anaconda from Anaconda.com.
2. Install Django `pip install django`
3. Install Pillow `pip install Pillow`
4. Install django-crispy-forms `pip install django-crispy-forms`
5. Install Pillow `pip install pylint-django`

## Usage

To start website/server run `python manage.py runserver`

## How to add field to database

If you want to add a field to the DCN database start by navigating to `blog/models.py/`, then add your field under the `Post` class.
After creating the new field you will need to migrate the database by running:

``` zsh
python manage.py makemigrations
python manage.py migrate
```

After this you can add the field to the website form by navigating to `blog/templates/post_form.html` and adding the field using `{{ form.field_name }}`.
