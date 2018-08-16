#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
pip install virtualenv
git clone https://github.com/josdavidmo/zinobe
cd "zinobe"
virtualenv --python /usr/bin/python env
source env/bin/activate
pip install -r requirements.txt
python manage.py create
python manage.py test
python manage.py run
