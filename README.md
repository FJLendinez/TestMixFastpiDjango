# TestMixFastpiDjango


To make it run:

```
python manage.py migrate   
DJANGO_SETTINGS_MODULE=ordermaker.settings uvicorn main:app --reload
```

Go to:

`http://127.0.0.1:8000/docs`

And enjoy :D

# User management

Now in this example we can signup and login easy and securely. You can test creating a user and log in `authorize` button or `token` endpoint


![image](/docs/images/OpenAPI.png)

## Permissions

There are 2 deps, one for authorize and another to check if user is admin. 

Check view `GET /` to see `get_current_user` dep.

Check view `POST /` to see `get_admin_user` dep.
