# Django REST API Instant view
This project is example of Single Page Application. Core of this project is React Component that show loaded data through http requests from API driven by Django REST Framework. Navigation implements with React Router 4. 

## Usage
First of all clone this repo on local machine into virtualenv:
```
$ virtualenv -p python3 project
$ cd project
$ source bin/activate
$ git clone https://github.com/conformist-mw/django_react
$ cd django_react
```
Now is required to install all django dependencies:
```
pip install -r requirements.txt
```
Migrations for database already made, so after setup `django_react/settings.py` you can migrate db:
```
python manage.py migrate
```
In User model implement staticmethod `_bootstrap()` that intended to populate database with fake data. To accomplish this run:
```
python manage.py shell
\>\>\> from instant.models import User
\>\>\> User._bootstrap()
```
This creates 300 rows of male persons, feel free to run with params `count` and `gender`.
Now just run django development server and open in browser [link](http://127.0.0.1:8000/)
```
python manage.py runserver
```
All done, it works.
# Development
If you want to make changes in `assets/js/index.jsx` it is required to setup npm:
```
$ sudo apt install npm
```
but may be it doesn't work as expected with npm from linux repositories. So you have to update it:
```
$ sudo npm install -g npm
$ sudo ln -s /usr/bin/nodejs /usr/bin/node
$ sudo npm install -g npm
```
Now run `npm install` in working directory. For futher setup see this [link](https://github.com/owais/django-webpack-loader)
In `package.json` available two commands:
```
npm run watch
npm run prod
```
first of it — live build while you edit `.jsx` file and second is build production version `main.bundle.js`.

## Useful links
* [Django project](https://www.djangoproject.com/)
* [Django REST Framework](http://www.django-rest-framework.org/)
* [Elizabeth](https://github.com/lk-geimfari/elizabeth)
* [React JS](https://facebook.github.io/react/)
* [React Router](https://reacttraining.com/react-router/web/guides/quick-start)
* [Webpack](https://webpack.js.org/)
* [Babel](https://babeljs.io/)
* [Axios](https://github.com/mzabriskie/axios)
