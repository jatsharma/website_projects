from django.contrib import admin
from django.urls import path
from . import views
app_name = 'photoapp'


urlpatterns = [
    path('',views.index,name='index'),
    path('<int:photo_id>/',views.detail,name='detail'),
]
