from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add', views.add ,name="add" ),
    url(r'^sub', views.sub ,name="sub" ),
    url(r'^more', views.more ,name="more" ),
    url(r'^details', views.details ,name="details" ),

]
