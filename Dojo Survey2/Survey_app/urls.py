from django.urls import path
from . import views

urlpatterns = [
    path('', views.form),
    path('process', views.process),
    path('results', views.results),
]