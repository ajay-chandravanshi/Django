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
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('services/',views.services,name='services'),
    path('book_event/',views.book_event,name='book_event'),
    path('book_room/',views.book_room,name='book_room'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    # for userdata use 
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
    path('edit/<int:pk>',views.edit,name='edit'),
    path('queryupdate/<int:pk>',views.queryupdate,name='queryupdate'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('search/<int:pk>',views.search,name='search'),
    # for query code end
    
    # admin dashboard code
    # path('admindash/<int:id>/<str:a_name>/<str:a_email>/<str:a_password>', views.admindash, name='admindash'),
    # path('admindash/', views.admindash, name='admindash'),
    path('admindash1/<int:ak>', views.admindash1, name='admindash1'),
    path('addcard/<int:cpk>/<int:pk>',views.addcard,name='addcard'),

    path('showcard/<int:ak>', views.showcard, name='showcard'),
    path('showcard/<int:pk>', views.showcard, name='showcard'),
    path('delete/<int:pk>/<int:cpk>',views.delete,name='delete'),

    path('home/<int:ak>',views.home2,name='home2'),
    path('about/<int:ak>',views.about2,name='about2'),
    path('contact/<int:ak>',views.contact2,name='contact2'),
    path('gallery/<int:ak>',views.gallery2,name='gallery2'),
    path('services/<int:ak>',views.services2,name='services2'),
    path('book_event/<int:ak>',views.book_event2,name='book_event2'),
    path('book_room/<int:ak>',views.book_room2,name='book_room2'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
