from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_transactions/', views.add_transactions, name='add_transactions'),
    path('income/delete/<int:income_id>/', views.delete_income, name='delete_income')
]