from django.urls import path
from .views import CreateUserView
from .apps import app_name

app_name = app_name
urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
]
