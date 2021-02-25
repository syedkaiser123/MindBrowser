# EMPLOYEE MANAGEMENT PROJECT

In this project manager can manage his employees,
1)Get the list of employees.
2)Create an employe.
3)Delete an employe.
4)Update employe details.

## Instructions :

1) install requirement.txt
    pip install -r requirements.txt
2) For initial setup create a Manager user
    Example:
        python manage.py create_manager_user -u "kaiser" -p "test" -f "syed" -l "kaiser" -a "Banglore" -d "1996-01-01" -c "new"
3) run migrations
    python manage.py makemigrations
    python manage.py migrate

4) Run project
    python manage.py runserver

## DIRECTORY STRUCTURE :

    .
    ├── api
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── utils
    │   │   └── permissions.py
    │   └── views.py
    ├── db.sqlite3
    ├── EmployeManagement
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── management
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── management
    │   │   └── commands
    │   │       └── create_manager_user.py
    │   ├── models.py
    │   ├── templates
    │   │   └── management
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    └── readme.md
