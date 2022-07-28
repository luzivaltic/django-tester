from . import views
from django.urls import path

urlpatterns = [
    path("", views.index , name="index"),
    path("binh" , views.binh , name="binh" ),
    path("<str:name>", views.greet , name="greet")
]