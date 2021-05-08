from django.urls import path
from . import views

urlpatterns = [
    path('', views.despesastest, name='despesas'),
]