# Run 
python manage.py createsuperuser

>it doesn't work

#Run 
python manage.py makemigrations
python manage.py migrate

# Now run 
python manage.py createsuperuser

###############################################
###############################################
# ADD models now
 blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



#in models.DateTimeField(##)

>auto_now =True
	makes date updated to whenever post updated

>auto_now_add =True
	it assigns date once post added...but that field can never be ALTERED

>default=timezone.now
	it assigns date once post added...but that field can be ALTERED


#  author = models.ForeignKey(User, on_delete=models.CASCADE) 
            >says to delete post if user is deleted


# Run
 python manage.py makemigrations
 python manage.py migrate



# Run
python manage.py sqlmigrate blog 0001

> to see SQL command it runned

###############################################
###############################################

python manage.py shell

>>> from blog.models import Post
>>> from django.contrib.auth.models import User



>>> User.objects.all()
<QuerySet [<User: doody>, <User: Testuser>]>


>>> User.objects.all().first()
<User: doody>


>>> User.objects.filter(username='doody')
<QuerySet [<User: doody>]>


>>> user=User.objects.get(username='Testuser')
>>> user
<User: Testuser>
>>> user.id
2


#using //User.objects.filter// returns a set
 where as //User.objects.get// returns object

#############################################################
#############################################################


>>> post1=Post(title ='Python Bootcamp',content ='crash course details',author_id =user.id)

#notice this carefully //author_id =user.id//

>>> post1
<Post: Python Bootcamp>

>>> post1.content
'crash course details'

post1.save()
>>> exit()

#############################################################
#############################################################

# in /views replace dummy posts with our model so do this.....

from .models import Post

def home(request):
+   posts =Post.objects.all()
    context  ={
        'posts' : posts
    }
    return render(request,'blog/home.html',context)


##########################################################
##########################################################
https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#date

<small class="text-muted">{{ post.date_posted|date:"D M Y" }}</small>


# to edit posts in admin we need to do...

from django.contrib import admin
from .models import Post

admin.site.register(Post)

##########################################################
##########################################################

# adding json file to add more posts at a time

https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Django_Blog/11-Pagination/django_project/posts.json

>add this .json file beside manage.py
   as posts.json


# now do this to load this values

python manage.py shell
 from blog.models import Post
>>> import json

>>> with open('posts.json') as f:
...     posts_json =json.load(f)
...
>>> for post in posts_json:
...     p=Post(title=post['title'],content=post['content'],author_id=post['user_id'])
...     p.save()
...
>>>
>>> exit()

$ python manage.py runserver

#now posts are added

