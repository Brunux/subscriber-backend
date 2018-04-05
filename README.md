# Subscriber Framework
A framework for Open Contracts standard. scalable, reliable and accessible.

- Helps Organizations and People find business opportunities  in order for them to offer products or services to tender winners by subscribing to the keys channels-feeds.
- Helps Enterprises find key contracts or procurements available.
- Generates advance statistics and analytics using Data Science order to map best contractors to fit in contracts base on achieves and good deliverables.

## Features

- Django 1.11
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Load environment variables from `.env` with [django-dotenv](https://github.com/jpadilla/django-dotenv).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.

## How to install

```bash
$ git clone git@github.com:Brunux/subscriber-backend.git
$ cd subscriber-backend
$ vim .env
$ pip install -r requirements.txt -r requirements/dev.txt
```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:dev
$ heroku addons:add newrelic
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
```

## License
The MIT License (MIT)
Copyright (c) 2012-2016 subscriber-framework team
