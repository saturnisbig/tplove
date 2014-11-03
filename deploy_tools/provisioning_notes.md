Provisioning a new site
=======================

## Required packages:

* nginx
* python
* Git
* pip
* virtualenv

eg, on Ubuntu:

    $ sudo apt-get install nginx git python-pip
    $ sudo pip install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|---sites
    |----SITENAME
         |--- database
         |--- source
         |--- static
         |--- virtualenv
