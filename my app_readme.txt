pip install virtualenvwrapper-win

mkvirtualenv py1 # to make pyi venv

workon py1  # to change to py1

lsvirtualenv     #from any where u can use this command,it lists the venvs

rmvirtualenv py1 #from any where u can use this command,it removes py1

deactivate

#Virtualenv is not bound to directory,
 from any where u can sign into it by giving venv(py1)name
#################################################################
#################################################################

pip install django

django-admin.py version

python -m django --version

django-admin startproject project1 .

#now manage.py is also created,so test running server by running
http://127.0.0.1:8000/    OR   http://localhost:8000/

# you can see install successful page

python manage.py startapp blog

#these are the contents of blog

				    admin.py
14-09-2019  22:20                88 apps.py
14-09-2019  22:20    <DIR>          migrations
14-09-2019  22:20                60 models.py
14-09-2019  22:20                63 tests.py
14-09-2019  22:20                66 views.py
14-09-2019  22:20                 0 __init__.py

#################################################################
#################################################################
# you can create bat file to open your pychrm(any app)

start "" "C:\Program Files\JetBrains\PyCharm Community Edition 2018.1.2\bin\pycharm64.exe"

# paste above in notepad and save as .bat
and double click .bat file to run it

# to get location of any app 
	> searcch in search bar
	> you can see shortcut
	> right click to open filelocation of (Shortcut)
	> now again right click to open filelocation of (app)
	> copy as text' the adress and paste in .bat as shown
#################################################################
#################################################################
#after opening pycharm..

# in blog app create urls.py file

#Note : app is added in installed_apps for 2 purposes as far as i know
	>to do migrations
	>to serch in templates folders of apps
# so right now no need to do still to add in installed_apps

# in blog/views.py ....

from django.http import HttpResponse
def home(request):
    return HttpResponse("hi i am creatig notes to entire django")

# in blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
]

# in project1/urls.py  make these changes(+)....

	from django.contrib import admin
+	from django.urls import path,include

	urlpatterns = [
	    path('admin/', admin.site.urls),
+	    path('blog/', include('blog.urls')),
	]

# and run server
python manage.py runserver

#in browser-check http://127.0.0.1:8000/blog/

#################################################################
#################################################################

# now we can use templates functionality

>add app in installed apps
     'blog.apps.BlogConfig',
 
# add templates folder in blog app
because django searches in all apps for templates directory


#in settings also include templatesfolder name to search for templates
'DIRS': [],
'DIRS': ['templates'],

#create dunmmy posts
 posts =[

    {'author' :'trivikram',
     'title':'jalsa',
     'content' : 'love story'
     'date_posted' : 'Aug 24 2019'},
    {'author' :'rajamouli',
     'title':'eega',
     'content' : 'animation story'
     'date_posted' : 'Aug 13 2009'}
]

# make changes in blog/urls.py 

urlpatterns = [
    path('', views.home),
+    path('about/', views.about),
]
#################################################################
#################################################################
def home(request):
    context  ={
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    context ={
        'title': 'About'
    }
    return render(request, 'blog/about.html',context)

#################################################################
#################################################################
blog/templates/blog/home.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}
        <title>Django -{{ title }}</title>
    {% else %}
        <title>Django</title>
    {% endif %}

</head>
<body>
{% for post in posts %}

<h1>{{post.title}}</h1>
<p>By {{post.author}} on {{post.date_posted}}</p>

{% endfor %}



</body>
</html>


#################################################################
#################################################################

blog/templates/blog/about.html

<body>

<h2>About Page</h2>

</body>

# and run server
python manage.py runserver

