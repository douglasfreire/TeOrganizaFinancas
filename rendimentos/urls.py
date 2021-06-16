from django.urls import path
from . import views


urlpatterns = [
    path('register-income/', views.income),
    path('list-income/', views.list_income),
    path('retrieve-income/<int:pk>/', views.retrieve_income),
    path('update-income/<int:pk>/', views.update_income),
    path('partial-income/<int:pk>/', views.partial_income),
    path('delete-income/<int:pk>/', views.delete_income)
]
