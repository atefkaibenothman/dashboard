# Dashboard
* An all-in-one dashboard for all of your needs

## Notes

### Django
* **Setting up project**
  * Create virtual environment
    * Install virtualenv `pip3 install virtualenv`
    * Create a virtual env `python3 -m venv venv`
    * Start virtual env `source venv/bin/activate`
  * Installing Django
    * `pip3 install Django`
    * Check version `python3 -m django --version`
  * Creating a project
    * `django-admin startproject [PROJECT_NAME]`
  * Create an app
    * `python3 manage.py startapp [APP_NAME]`

* **Running project**
  * `python3 manage.py runserver`

* **Migrations**
  * `python3 manage.py migrate`

* **Order of operations**
  * client -> project urls.py -> app urls.py -> app views.py


### Graphene-Django
* **Setting up graphene**
  * Install `pip3 install graphene-django`
  * Add `graphene_django` into installed apps in project


### Apollo-React-Graphql
* **Setting up apollo**
  * Install `npm install @apollo/client` and `npm install graphql`


### Postgres
* **Setting up postgres**
  * Install postgres `pip3 install psycopg2 psycopg2-binary postgresql`
  * Connect to posgres using premade 'postgres' role `sudo -i -u postgres`

* **Commands**
  * show databases `\l`
  * choose database `\c [DB_NAME]`
  * show tables `\dt`


### React
* Setting up project 
  * Create new django app for frontend
  * Initialize package.json `npm init -y`
  * Initialize webpack
    * JS module bundler
  * Initialize babel
    * Used to convert ECMAScript into a backwards compatible version of JS
