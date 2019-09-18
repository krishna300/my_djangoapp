# Now start blocking html codes


blog/templates/blog/home.html

{%extends 'blog/base.html'%}

{% block content %}
    {% for post in posts %}
        <h1>{{post.title}}</h1>
        <p>By {{post.author}} on {{post.date_posted}}</p>

    {% endfor %}
{% endblock content %}

##################################################
##################################################

blog/templates/blog/about.html
{%extends 'blog/base.html'%}

{% block content %}

<h2>About Page</h2>
{% endblock content %}
##################################################
##################################################
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
<h1>I am using extend functionality</h1>
{% block content %} {% endblock content  %}
</body>
</html>

##################################################
##################################################
# add main block in body of base.html

<main role="main" class="container">
      <div class="row">
        <div class="col-md-8">
          {% block content %}{% endblock %}
        </div>
        <div class="col-md-4">
          <div class="content-section">
            <h3>Our Sidebar</h3>
            <p class='text-muted'>You can put any information here you'd like.
              <ul class="list-group">
                <li class="list-group-item list-group-item-light">Latest Posts</li>
                <li class="list-group-item list-group-item-light">Announcements</li>
                <li class="list-group-item list-group-item-light">Calendars</li>
                <li class="list-group-item list-group-item-light">etc</li>
              </ul>
            </p>
          </div>
        </div>
      </div>
    </main>

##################################################
##################################################

# add nav block in body of base.html

<header class="site-header">
      <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
          <a class="navbar-brand mr-4" href="#">Django Blog</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav mr-auto">
              <a class="nav-item nav-link" href="#">Home</a>
              <a class="nav-item nav-link" href="#">About</a>
            </div>
            <!-- Navbar Right Side -->
            <div class="navbar-nav">
              <a class="nav-item nav-link" href="#">Login</a>
              <a class="nav-item nav-link" href="#">Register</a>
            </div>
          </div>
        </div>
      </nav>
    </header>


##################################################
##################################################

# add directory like blog/static/blog/main.css

# in base.html add lines
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">


##################################################
##################################################
# in blog/home.html replace for loop code with this...for good looking


<article class="media content-section">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="#">{{ post.author }}</a>
              <small class="text-muted">{{ post.date_posted }}</small>
            </div>
            <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>

# python manage.py runserver 

##################################################
##################################################

# add href as shown in nav bar
 
<a class="nav-item nav-link" href=" {% url 'home' %}">Home</a>
<a class="nav-item nav-link" href="{% url 'about' %}">About</a>





















