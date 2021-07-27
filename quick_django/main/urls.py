
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('temp', views.temp, name="temp"),
    path('list', views.list, name="list"),
    path('rel', views.rel, name="rel"),
    path('rel2', views.rel2, name="rel2"),
    path('form_input', views.form_input, name="form_input"),
    path('form_process', views.form_process, name="form_process"),
]
