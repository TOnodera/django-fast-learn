
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('temp', views.temp, name="temp"),
    path('list', views.list, name="list"),
    path('rel', views.rel, name="rel"),
    path('rel2', views.rel2, name="rel2"),
]
