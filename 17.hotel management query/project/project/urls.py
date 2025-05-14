"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('services',views.services,name='services'),
    path('book_event',views.book_event,name='book_event'),
    path('book_room',views.book_room,name='book_room'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),

    path('home/<int:pk>',views.home1,name='home1'),
    path('about/<int:pk>',views.about1,name='about1'),
    path('contact/<int:pk>',views.contact1,name='contact1'),
    path('gallery/<int:pk>',views.gallery1,name='gallery1'),
    path('services/<int:pk>',views.services1,name='services1'),
    path('book_event/<int:pk>',views.book_event1,name='book_event1'),
    path('book_room/<int:pk>',views.book_room1,name='book_room1'),
    path('dashboard/<int:pk>',views.dashboard,name='dashboard'),
    
    # for query code start
    path('query/<int:pk>',views.query,name='query'),
    path('allquery/<int:pk>',views.allquery,name='allquery'),
    
    # for query code end
    
]
