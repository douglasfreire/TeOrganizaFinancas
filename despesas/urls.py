from django.urls import path
from . import views
from .views import ExpensesAPIView, ExpenseDetailApiView

urlpatterns = [
    path('', views.despesastest, name='despesas'),
    path('list-expenses/', ExpensesAPIView.as_view()),
    path('register-expense/', ExpensesAPIView.as_view()),
    path('retrieve-expenses/<int:pk>/', ExpenseDetailApiView.as_view()),
    path('update-expense/<int:pk>/', ExpenseDetailApiView.as_view()),
    path('partial-expense/<int:pk>/', ExpenseDetailApiView.as_view()),
    path('delete-expense/<int:pk>/', ExpenseDetailApiView.as_view())
]
