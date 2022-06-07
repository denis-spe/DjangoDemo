# Import library
from . import views                         
from django.urls import path

# Construct a urlpatterns
urlpatterns = [
    path(route="", view=views.index, name="index")
]

