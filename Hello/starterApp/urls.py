# Import library
from . import views                         
from django.urls import path

# Instantiate the App name
app_name = "starterApp"

# Construct a urlpatterns
urlpatterns = [
    path(route="", view=views.index, name="index"),
    path(route="register", view=views.register,
    name="register"),
    path(route='login', view=views.login, name='login')
]

