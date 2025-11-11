[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-cPJVYMd)
Django ORM Standalone
=====================

# SOFE3650 Assignment 3: Django Frameworks and Energy Quality Attribute
**Group 12**
+ Drew Glover - 100914229
+ Reid Hillis - 100915844
+ Ebubechukwu Agwagah - 100937022

Q1
-------------------
a. <br>
The models.py file was modified to change the sample user model to a product model. Modified it from just a name field to having a UPC, name, and price field. Then, the main.py file was modified from seeding users to seeding the products. This was done using a get_or_create statement instead of create so that duplicates are not created each run. Finally, all products info was printed.

b. <br>
The main.py file was modified to prompt the user for an input, if the input is valid and matches one of the UPC's in the system it will output the item name and price. If the input is not valid the system it will output "Product not found. Please try again.".

Application being used:
<img width="862" height="306" alt="image" src="https://github.com/user-attachments/assets/f64c9113-e34e-4d3e-91c3-059f3d21ac3e" />

Q2
-------------------
a. <br>
<img width="791" height="379" alt="image" src="https://github.com/user-attachments/assets/289a1863-7bfe-40e6-babf-2f9200651862" />

b. <br>
The first architectural or design tactic that could improve energy efficiency in our scenario is the schedule resources tactic. This would be applied by having the health monitoring app perform tasks that need a lot of energy like data uploads or report generation, only at certain times. For example, when the phone is charging or connected to Wi-Fi. This helps to reduce the number of times the device processors are activated, which gives more consistent power consumption.

The second...


| Group Member  | Responsibility |
| ------------- | ------------- |
| Reid Hillis   | Q1 A & Q2 B  |
| Drew Glover   | Q1 B & Q2 B  |
| Ebubechukwu Agwagah  | Q2 A  |

![Django](https://img.shields.io/badge/Django_ORM-Standalone-blue)
![Python](https://img.shields.io/badge/Python-yellow)

Use the database components of Django without having to use the rest of Django (i.e. running a web server)! :tada: A typical use case for using this template would be if you are writing a python script and you would like the database functionality provided by Django, but have no need for the request/response functionalty of a client/server web application that Django also provides. 

With this project template you can write regular python scripts and use Django's excellent ORM functionality with the database backend of your choice. This makes it convienient for Djangonauts to write database driven python applications with the familiar and well polished Django ORM. Enjoy.

:gear: Requirements
-------------------
- Last tested successfully with Python 3.10.4 and Django 5.0.6
- Create venv and pip install django to import the required modules.

:open_file_folder: File Structure
---------------------------------
```
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── main.py
├── manage.py
├── README.md
└── settings.py
```

__The main.py file is the entry point for the project, and where you start your code. You automatically get access to your models via ```from db.models import *```
Think of it like a plain old python file, but now with the addition of Django's feature-rich models.__ :smiling_face_with_three_hearts:

__The db/models.py is where you configure your typical Django models.__ There is a toy user model included as a simple example. After running the migrations command in the quick setup below, a db.sqlite3 file will be generated. The settings.py file is where can swap out the sqlite3 database for another database connection, such as Postgres or AmazonRDS, if you wish. For most applications, sqlite3 will be powerful enough. But if you need to swap databases down the road, you can easily do so, which is one of the benefits of using the Django ORM. 

:rocket: Quick Setup
--------------------
Create a folder for your project on your local machine
```
mkdir myproject; cd myproject
```
Create a virtual environment and install django
```
python -m venv venv; source venv/bin/activate; pip install django
```
Download this project template from GitHub
```
git clone git@github.com:dancaron/Django-ORM.git; cd Django-ORM
```
Initialize the database
```
python manage.py makemigrations db; python manage.py migrate
```
Run the project
```
python main.py
```

Feel free to send pull requests if you want to improve this project.

:crystal_ball: Example
----------------------
After running Quick Start above: 

Code in db/models.py:
```
# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default='Dan')

    def __str__(self):
        return self.name
```
Code in main.py:
```
# Seed a few users in the database
User.objects.create(name='Dan')
User.objects.create(name='Robert')

for u in User.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')
```
Output from command: ```python main.py```
```
ID: 1	Username: Dan
ID: 2	Username: Robert
```

:mortar_board: Django Models
----------------------------

Link: [How to Use Django Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

License
-------

The MIT License (MIT) Copyright (c) 2024 Dan Caron

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
