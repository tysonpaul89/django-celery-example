# django-celery-example
* This is a example project to demostrate the working of scheuled tasks using Celery
* I am using Celery to run a delayed task, Celery Beat to run periodic task and Celery Flower to monitor the task.
* For celery backend, I am using Redis.

To install redis:
```
sudo apt install redis-server 
```

To install depedancy packages of pipenv:
```
pipenv install
```
Once everything is installed using the following terminal command in the python environment

To start worker process with celery only:(To run delayed jobs only)
```
celery -A dj_celery worker -l info
```

To start worker process with celery and beat:(To run delayed and periodic job at the same time)
```
celery -A dj_celery worker -l info -B
```

### Credits:
https://medium.com/@markgituma/using-django-2-with-celery-and-redis-21343284827c

https://medium.com/@yehandjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7
