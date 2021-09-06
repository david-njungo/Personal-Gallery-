from django.conf.urls import url
from . import views

url patterns =[
    url(r'^$',views.home,name='home'),
]