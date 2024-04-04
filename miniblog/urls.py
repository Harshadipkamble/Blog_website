"""
URL configuration for miniblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dash,name='dash'),
    path('up/',views.user_signup,name='up'),
    path('in/',views.user_login,name='in'),
    path('out/',views.user_logout,name='out'),
    path('addpost/',views.add_post,name='addpost'),
    path('updatepost/<int:id>/',views.edit_post,name='updatepost'),    
    path('delete/<int:id>/',views.delete_post,name='delete'),    
   path('ticket-form/', views.ticket_form_view, name='ticket_form'),
]
