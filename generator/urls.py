from django.urls import path
from .views import homePageView, password, about

urlpatterns = [
    path('', homePageView, name='home'),
    path('password/', password , name='password'),
    path('about/', about, name='about'),
]