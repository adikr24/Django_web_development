# Django_web_development
Web development using Django


## download django
## getting started in django
## cd C:\Users\adity\python_install\Scripts 
## django-admin startproject website

##always ignore manage.py
## settings--> options for your website

## starting the development server
## make sure you're in the directory and then 
## cd .\website.py (name of my file)
## ls
to make sure manage.py is there
then
## python manage.py runserver
## Development server starts


#### to develop an app in django
python manage.py startapp music (name of the app in django)

## workflow

-- create a project  from django-admin
-- create an app if req
-- change the settings to look for the app
-- Change the url to direct to certain page
-- If there's gonna be too many url then don't clutter host/url instead create  a url inside app and make url(host) look into the url(app)
-- Migrate the changes to validate the code
-- Blue Print of the database is required
-- Upon deciding the db, create classes to store data as columns in SQL (default)
-- migrate to reflect changes
-- register the models.py (where the blue print of the data is stored into the admin.py page)
--Create superuser to login to admin site and visualize the backend of db
-- create urls for the homepage
-- get HTTP Response from the user, forward the request to views.py , read and write data from models.py and return the response --> HTML

App sections in python
## admin section --> section where you can go and edit db and login permissions etc
## models.py --> how to store data in django(LIKE A BLUE PRINT) (like one class for songs and another for albums)
## test --> to create your testcases for your data
## views.py --> views are just python function that take reqs from user and perform actions

## whatever URLS we want for the music section 
we wanna stick in urls.py file in the music section so as we just do one import in the urls in website folder


##############################After setting up the database now
python manage.py shell
## opens up the python shell for prog
#######Coding in Shell
## import music model ## the database
from music.models import Album, Song
## see what's there in the dba
Albums.object.all()
## writing to a dba 
a= Album(artist = "Taylor Swift",album_title= "Red", genre = "Country", album_logo = "www.google.com")
## to save from shell to dba
a.save()
## to review the data
a.artist
a.pk or a.id ##gives the primary key of the data

########################Creating an admin login in django
go to the home directory
--> command promt-- which python
--> type the dir -- python manage.py create superuser
enter admin name, email and password
login to the default webserver

-->http://localhost:8000/admin
--> enter user name and password

#########################
## change the admin page if you want something to appear on the database
### mixing html with python

def index(request): ## the name of the index should be constant throughout
	## connect to the database and get all the albums
	all_albums= Album.objects.all() ## store the information of all albums 
	## loop through all albums
	html = ''
	for album in all_albums:
		url= '/music/' + str(album.id) + '/'
		html += '<a href ="' + url + '">' + album.album_title + '</a><br>'
	return HttpResponse(html)

##################### adding or deleting attributes will need migration in django
## python manage.py makemigrations music ## command line prompt for changes in the model
###########TEMPLATES

Most of the HTML and navigation structure will be the same in every page of out site so instead of duplicating the boilerplate code on every page 
we use django templating language to declare a base template

## use extend and block unblock template to change the standard boilerplate code

## foreign ekey
like each song will be linked to album so let's say an album has a primary key of 1 and it links with songs, so the song has foregin key of 1 
#primary key --> something unique
## foreign key --> something that is a part of the unique element
## on_delete --> models.CASCADE

### make migrations after changing the model
## migration is a change to your database
commands to make migrations 
python manage.py makemigrations music ## creates files for migrations
python manage.py sqlmigrate music 0001 ## creates columns for migrations
python manage.py migrate ## applies migrations

## Anytime you wanna make a change --> makemigrations and migrate

### templates and contexts
Contexts is simply a set of variables and their associated values. A template uses context to populate its variable tags and evaluate it's block tags.

Example
from django.template import Context, Template
t= Template("My name is {{ name }}.")
c= Context ({"name": "Stephane"})
t.render(c)
--> my name is stephane

########### templates and render function ###########################################################
from django.template import Template, Context
person = {'name':'Sally', 'age': '43'}
t = Template('{{ person.name.upper }} is {{ person.age }} years old.')
c = Context({'person': person})
t.render(c)
----> SALLY is 43 years old
############################## if else function django
{% if xyz %}
condition
{% else %}
condition
{% endif %}
--> multiple if statments can be used but you can't use if - elif statement like normal python
#########################LOOPS
forloop.counter
{% for item in todo_list %}
<p> {{ forloop.counter }} : {{ item }} </p>
{% endfor %}
########################## forloop.counter0 starts with 0 if replaced by the above forloop.counter
########################## forloop.revcounter starts with the remaining number of itmes and rev back to 0
########################## forloop.first --> boolean value set to True if it's the first value we're looking
{% for country in countries %}
<table>
{% for city in country.city_list %}
<tr>
<td>Country #{{ forloop.parentloop.counter }}</td>
<td>City #{{ forloop.counter }}</td>
<td>{{ city }}</td>
</tr>
{% endfor %}
</table>
{% endfor %}
## parentloop.counter trace backs the parentloop when inside the 
{% ifequal %} comparison tag
{# THIS is A Comment #}-> comment tag

#### Filters
{{ name|lower }}
this displays the value of the {{ name }} variable after being filtered through the lower filter
{{ my_text|escape|linebreaks }}
{{ bio|truncate:"30" }}
--> displays the first 30 words of the bio variable
###### MVC 
M- model
V- view
C - controller
The MVC Development Pattern 
M - data access portion (handled by django's database layer)
V - the portion that selects which data to display and how to display it (handled by views and templates)
C - the portion that delegates to a view depending on user input
Because C is handled by the framework itself and most of the excitement in django happens in models, templates and views. Django has been referred to as MTV framework
T - stands for template 
V - views
Django is MTV development framework
#######################################DJANGO's databases
--> check to see if django's db is configured or not
from django.db import connection
cursor = connection.cursor()







