LOGIN  & LOGOUT

# login and logout class based views provide forms and user all...
but template need to be provided


#in project/urls  
>add these 3 lines ....

from django.contrib.auth import views as auth_views


path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),



## IF template_name is not passed to view it searches somewhere else


>now create login & logout template

# LOGIN TEMPLATE


>Observe it is edited version of register.html


{%extends 'blog/base.html'%}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Log in</legend>
                {{ form|crispy}}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login now</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Need An Account? <a class="ml-2" href="{%url 'register'%}">Sign Up</a>
            </small>
        </div>
    </div>


{% endblock %}


# after login it dont 'have' 
where to redirect so error occurs

> in settings.py add

LOGIN_REDIRECT_URL = 'home'
###########################################################
###########################################################


LOGOUT 
>TEMPLATE IS EDITED FORM OF LOGIN

{%extends 'blog/base.html'%}
{% load crispy_forms_tags %}
{% block content %}
    <h2>Yoyu have been Logged Out !</h2>

        <div class="border-top pt-3">
            <small class="text-muted">
                 <a class="ml-2" href="{%url 'login'%}">Login Again</a>
            </small>
        </div>

{% endblock %}

##################################################################
##################################################################

Profile :

#users/views.py

def profile(request):
    return render(request,'users/profile.html')

# no need to pass user as context ::


#project/urls :

  path('profile/', user_views.profile,name ='profile'),


#users/template/users/profile.html:

{%extends 'blog/base.html'%}

{% block content %}
    <div class="content-section">


        <h2>{{user.username}}</h2>
    </div>


{% endblock %}

############################################################
# but to make sure when logged_out 
 if u access profile manually it goes to that page  and shows no user

#instead it should ask for login 
 so ..use login decoratotors...above profile view

from django.contrib.auth.decorators import login_required
 @login_required

#########################################################

# also u should say where to look for login url in settings
#project/settings:

LOGIN_URL = 'login'




##################################################################
##################################################################


# but my problem is even you are logged out you can acces home page/about page
# even you are logged in u can again login/register


# so what happened is when u logout u are really logged out...
because logout is a class based view with certain logic 
u can check it because 
	if logged in and access profile page it shows username
	if logged out and access profile it dont show any user name......
but to make SOMEPAGES/(profile/home/about whatever u want)/ make available only 
if u are logged in then use >>>>    **DECORATORS**

















