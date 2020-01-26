from django.urls import path
from . import views




urlpatterns = [
    path('text/<user_text>', views.cool_text),
    path('about', views.about),
    path('', views.index),
    path('hello/<name>', views.name),


]
