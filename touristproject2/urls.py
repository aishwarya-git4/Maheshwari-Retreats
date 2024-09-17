"""
URL configuration for touristproject2 project.

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
from touristapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('package/',views.package,name='package'),
    path('booking/',views.booking,name='booking'),
    path('northindia/',views.northindia,name='northindia'),
    path('southindia/',views.southindia,name='southindia'),
    path('international/',views.international,name='international'),
    path('asia/',views.asia,name='asia'),
    path('europe/',views.europe,name='europe'),
    path('india/',views.india,name='india'),
    path('membership/',views.membership,name='membership'),
    path('error/',views.error,name='error'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact/',views.contact,name='contact'),
    path('membershippaid/',views.membershippaid,name='membershippaid'),
    path('search/',views.search,name='search'),
    path('bookingpaid/',views.bookingpaid,name='bookingpaid'),
    path('bookingpaid/index',views.index,name='index'),
    path('northindia/kanatal.html',views.kanatal,name='kanatal'),
    path('northindia/mussoorie.html',views.mussoorie,name='mussoorie'),
    path('northindia/shimla.html',views.shimla,name='shimla'),
    path('northindia/janjehli.html',views.janjehli,name='janjehli'),
    path('southindia/poovar.html',views.poovar,name='poovar'),
    path('southindia/munnar.html',views.munnar,name='munnar'),
    path('southindia/ooty.html',views.ooty,name='ooty'),
    path('southindia/kodaikanal.html',views.kodaikanal,name='kodaikanal')
    
    
]
