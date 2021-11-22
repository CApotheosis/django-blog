## Django commnds:
- django-admin startproject name: to create basic django app template
- python manage.py migrate: to migrate created models into db. Each data model is mapped to a database table.
- python manage.py runserver: strats development server
- python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings: to run the Django development server on a custom host and port or tell Django to load a specific settings file
- python manage.py startapp blog: create new app
- python manage.py makemigrations blog: applies migration (updates db according to models state)
- python manage.py sqlmigrate blog 0001: sqlmigrate commands takes migration names and returns SQL without executing it.
- python manage.py migrate: applies existing migrations

## Created app folder structure:
- manage.py: This is a command-line utility used to interact with your project. It is a thin wrapper around the django-admin.py tool.
- mysite/: This is your project directory, which consists of the following files:
- __init__.py: An empty file that tells Python to treat the mysite directory as a Python module.
- asgi.py: This is the configuration to run your project as ASGI, the emerging Python standard for asynchronous web servers and applications.
- settings.py: This indicates settings and configuration for your project and contains initial default settings.
- urls.py: This is the place where your URL patterns live. Each URL defined here is mapped to a view.
- wsgi.py: This is the configuration to run your project as a Web Server Gateway Interface (WSGI) application.


### When you have to deal with multiple environments that require different configurations, you can create a different settings file for each environment.


Django settings file by default:
- Debug: when True, prints fail info. Set to False on production
- ALLOWED_HOSTS: hosts with access to this service. Inactive while testing or on Debug=True
- INSTALLED_APPS is a setting you will have to edit for all projects. Default:
    - django.contrib.admin: An administration site
    - django.contrib.auth: An authentication framework
    - django.contrib.contenttypes: A framework for handling content types
    - django.contrib.sessions: A session framework
    - django.contrib.messages: A messaging framework
- ROOT_URLCONF: indicates the Python module where the root URL patterns of your application are defined.
- DATABASES is a dictionary that contains the settings for all the databases to be used in the project. There must always be a default database.

For more info: https://docs.djangoproject.com/en/3.2/ref/settings/

## App structure:
- admin.py: This is where you register models to include them in the Django administration site—using this site is optional.
- apps.py: This includes the main configuration of the blog application.
- migrations: This directory will contain database migrations of your application. Migrations allow Django to track your model changes and synchronize the database accordingly.
- models.py: This includes the data models of your application; all Django applications need to have a models.py file, but this file can be left empty.
- tests.py: This is where you can add tests for your application.
- views.py: The logic of your application goes here; each view receives an HTTP request, processes it, and returns a response.

## Commands used to build model:
- title: This is the field for the post title. This field is CharField, which translates into a VARCHAR column in the SQL database.
- slug: This is a field intended to be used in URLs. A slug is a short label that contains only letters, numbers, underscores, or hyphens. You will use the slug field to build beautiful, SEO-friendly URLs for your blog posts. You have added the unique_for_date parameter to this field so that you can build URLs for posts using their publish date and slug. Django will prevent multiple posts from having the same slug for a given date.
- author: This field defines a many-to-one relationship, meaning that each post is written by a user, and a user can write any number of posts. For this field, Django will create a foreign key in the database using the primary key of the related model. In this case, you are relying on the User model of the Django authentication system. The on_delete parameter specifies the behavior to adopt when the referenced object is deleted. This is not specific to Django; it is an SQL standard. Using CASCADE, you specify that when the referenced user is deleted, the database will also delete all related blog posts. You can take a look at all the possible options at https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete. You specify the name of the reverse relationship, from User to Post, with the related_name attribute. This will allow you to access related objects easily. You will learn more about this later.
- body: This is the body of the post. This field is a text field that translates into a TEXT column in the SQL database.
- publish: This datetime indicates when the post was published. You use Django's timezone now method as the default value. This returns the current datetime in a timezone-aware format. You can think of it as a timezone-aware version of the standard Python datetime.now method.
- created: This datetime indicates when the post was created. Since you are using auto_now_add here, the date will be saved automatically when creating an object.
- updated: This datetime indicates the last time the post was updated. Since you are using auto_now here, the date will be updated automatically when saving an object.
- status: This field shows the status of a post. You use a choices parameter, so the value of this field can only be set to one of the given choices.


### The Meta class inside the model contains metadata. ordering set to "publish" which means to sort querying db in descending order with "-".

## In order for Django to keep track of application, we need to add out app to the INSTALLED_APPS setting

### Django generates the table names by combining the application name and the lowercase name of the model (blog_post), but you can also specify a custom database name for your model in the Meta class of the model using the db_table attribute.

### Django creates a primary key automatically for each model, but you can also override this by specifying primary_key=True in one of your model fields.