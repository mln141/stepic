sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/hello.py  /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
cd web
#django-admin startproject ask
#python manage.py startapp qa
#sudo gunicorn -b 0.0.0.0:8080 hello:hello
#sudo gunicorn -b 0.0.0.0:8000 hello:hello
#sudo gunicorn -b 0.0.0.0:8000 ask:qa 

cd /home/box/
