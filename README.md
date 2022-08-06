# web-api-votage-unbalance

A web API for a IoT project. The IoT project is about voltage unbalance reduction in low voltage feeder by dynamic switching among electric loads using IoT. Built using DjangoRESTFramework, the API stores the RYB parameters of the line. As well as, toggle the IoT devices remotely with a simple built website using Bulma Framework of CSS.

### Backend

Set up virtual environment and install the dependencies using the commands:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then run the Django development server using:

```
python manage.py runserver
```

To create a superuser (admin) account, run:

```
python manage.py createsuperuser
```

API can be accessed through the base url `http://localhost:8000`.
