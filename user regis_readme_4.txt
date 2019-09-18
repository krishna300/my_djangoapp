# user registration

>create an users app

python manage.py startapp users

#go to project/urls

from django.contrib import admin
+ from django.urls import path,include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
+   path('register/', user_views.register),
    path('', include('blog.urls')),
]

#######################################################################
#######################################################################

#go to users/views 

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# Create your views here.

def register(request):
    if request.method =='POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username} !')
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request,'users/register.html',{'form' : form})


#go through above query so you can understand it !


##########################################################
##########################################################

in blog/base.html  add this 
line before content block toget messages ....


{% if messages %}
            {% for message in messages %}
              <div class="alert alert-{{ message.tags }}">
                {{ message }}
              </div>
            {% endfor %}
          {% endif %}














# in users/register.html

{%extends 'blog/base.html'%}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Join Today</legend>
                {{ form|crispy}}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Sign Up</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Already Have An Account? <a class="ml-2" href="#">Sign In</a>
            </small>
        </div>
    </div>


{% endblock %}



# install crispy using pip....
pip install django-crispy-forms


# in installed apps add......'crispy_forms',

# in settings add.....   CRISPY_TEMPLATE_PACK = 'bootstrap4'

# in users/register.html do....
{% load crispy_forms_tags %}
{{ form|crispy}}
#######################################################################
#######################################################################

# add name to register url as..... 
name ='register'

# add link to register button in nav bar in blog/base.html
href="{% url 'register' %}"


# in users/view
 retun is placed wrongly (in else)...
it should be places commonly to if and else


#######################################################################
#######################################################################

#if need to edit form you have to do this ....
like if you want @email in form

>create forms.py in users/

$$
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#and in users/views...

from .forms import UserRegisterForm

# and replace UserCreationForm with UserRegisterForm



#######################################################################
#######################################################################

# i added 
>doody id = 1
>Testuser 2
>food 3 (not staff,not admin)


then deleted food(no posts included)

then deleted Testuser( posts related to Testuser deleted)


# i again added 
>apple 4 (super,staff)


#######################################################################
#######################################################################

# Reset Password

C:\dir1>python manage.py shell

>>> from django.contrib.auth.models import User

>>> y=User.objects.get(username ='Testuser')
>>> y
<User: Testuser>

>>> y.set_password('vamsi@2019')

>>> y.save()

>>> exit()
