from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="home"),
    path('about', about, name="about"),
    path('category', category, name="category"),
    path('blog', blog, name="blog"),
    path('contact', contact, name="contact"),
]
