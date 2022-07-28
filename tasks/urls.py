from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index , name="index"),   
    path("something", views.add , name="something" ),
]