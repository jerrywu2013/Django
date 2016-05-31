#Deploy Django 1.7 with Python3 on Ubuntu 14.04

##Virtual Environment
###python2
```
sudo apt-get update
sudo apt-get install python-pip apache2 libapache2-mod-wsgi
```
###python3
```
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```

###Configure Virtual Environment
```
sudo pip install virtualenv
mkdir myproject
cd myproject
virtualenv myprojectenv
source myprojectenv/bin/activate
```

###Create Django Project
```
django-admin.py startproject mysite
```
###Add a line to configure this directory.
```
nano mysite/settings.py
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```
###Complete initial project 
```
cd mysite
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
./manage.py runserver 0.0.0.0:8000
```

##Apache

