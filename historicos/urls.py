from django.urls import path

from historicos import views

urlpatterns = [
    path('register-historic/', views.income),
    path('list-historic/', views.list_income),
    path('retrieve-historic/<int:pk>/', views.retrieve_income),
    path('update-historic/<int:pk>/', views.update_income),
    path('partial-historic/<int:pk>/', views.partial_income),
    path('delete-historic/<int:pk>/', views.delete_income)
]