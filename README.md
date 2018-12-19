django_es_example
=================

A small example of how to optimize search by Django + Elasticsearch.

## Use

### 1.clone build up 

```
git clone git@github.com:willdx/django_es_example.git
cd django_es_example
docker-compose -f local.yml build
docker-compose -f local.yml up
```

### 2.create super user

```
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

### 3.update models config

When model changes after the container is started.

```
docker-compose -f local.yml run --rm django python manage.py makemigrations&&python manage.py migrate
```

### 4.shutdown

When the whole test is complete.

```
docker-compose -f local.yml down
```

## result

**add user data**

http://localhost:8000/api/user/

![sudents_demo_add_user](http://iwillb.imdancer.com/sudents_demo_add_user.png)


**search user data**

http://localhost:8000/search/?keyword=admin

![django_es_example_search](http://iwillb.imdancer.com/django_es_example_search.png)



## Getting Up and Running Locally With Docker detailed

[deployment-with-docker](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)


## Detailed implementation steps

[arwrite: Django最佳实践_使用ElasticSearch优化搜索](http://rw.imdancer.com/read/249/)
