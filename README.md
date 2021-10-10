# Stores API

Stores is a RestFull API that connect with MySQL and allows to create users, get, save and delete 
stores and get, save, edit and delete store items. The content of this project is only for educational purposes.

## How to run this project

* This project use **Pipenv**. You can read the docs [here](https://pipenv-es.readthedocs.io/es/latest/).
* You need to modify the database connection inside **.env** with your database credentials and the database name.
The tables will be created automatically before the first request will be executed.
* The unit test are written with **Pytest**. You can run a test file with the following command
```
pytest filename.py
```
or the whole test collection with 
```
pytest *
```
You should run these commands in the terminal and inside the test folder.
* When you run the project you can visit `http://localhost:5000/apidocs` to view the swagger documentation.

## How to use Stores API

* Stores API can be consumed by the following
[repository](https://github.com/pablobascunana/stores-vue3) that is a web page created with vue3 that allow you
to create users, get, save and delete stores and get, save, edit and delete store items.
* Also you can consume the API using Postman importing the following
[collection](https://www.getpostman.com/collections/c34402699649f5337d0b).
