from django.urls import path

from historicos import views

urlpatterns = [
    path('register-historic/', views.HistoriesAPIView.as_view()),
    path('list-historic/', views.HistoriesAPIView.as_view()),
    path('retrieve-historic/<int:pk>/', views.HistoriesDetailAPIView.as_view()),
    path('update-historic/<int:pk>/', views.HistoriesDetailAPIView.as_view()),
    path('partial-historic/<int:pk>/', views.HistoriesDetailAPIView.as_view()),
    path('delete-historic/<int:pk>/', views.HistoriesDetailAPIView.as_view())
]