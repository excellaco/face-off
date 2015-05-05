Face-Off ![Build Status](https://travis-ci.org/excellalabs/face-off.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/excellaco/face_it/badge.svg)](https://coveralls.io/r/excellaco/face_it)

=======================

A Yammer/Django Application application built for the gamification of learning the names of your fellow colleagues. The hardest part of starting a with a new company is putting names to faces and so this application can be used to ease the onboarding of new employees.

# Application Hosting
-----
### 1. Yammer Client Application
* [Register An App With Yammer](https://developer.yammer.com/v1.0/docs/app-registration)


### 2. Development Environment Setup
* Clone this repo
* Copy `face_it/settings/local.py.example` to `face_it/settings/local.py`
* Add your keys (created in step 1) to `face_it/settings/local.py`
* Install [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/)
* Initialize the vagrant box - `vagrant up`
* Log into the server - `vagrant ssh`
* Create a super user using the command `python manage.py createsuperuser`
* Install & Start [Redis Cache server](http://redis.io/) prior in a separate shell - `redis-server` 
* Launch the app - `python manage.py runserver 0.0.0.0:8000`
* Access the app in your browser - `http://localhost:8111`

### 3. Heroku Deployment (Optional)
* `heroku create {appName}`
* `heroku config:add BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git`
* `git push heroku master`
* `heroku addons:add heroku-postgresql`
* Create a [RedisToGo](https://redistogo.com) account
    * `heroku addons:add redistogo`
    * `heroku config:add REDISTOGO_URL={instanceName}` 
        *  i.e instanceName = redis://redistogo:xxxx@test.redistogo.com:10355/
* `heroku ps:scale web=1`
* `heroku run python manage.py syncdb`

## Tests
---
### Unit Tests
* Load test fixture data `./manage.py loaddata "core/fixtures/core-test.json"`
    * Applying fixtures pushes pre-populated data into your application.
* Run unit-tests - `python manage.py test`
 
#### Selenium Tests w/ Behave
* start behave instance - `behave core/features`



