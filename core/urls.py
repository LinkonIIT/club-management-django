from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Member
    path('member/add/', views.add_member, name='add_member'),
    path('member/edit/<int:pk>/', views.edit_member, name='edit_member'),
    path('member/delete/<int:pk>/', views.delete_member, name='delete_member'),

    # Payment
    path('payment/add/', views.add_payment, name='add_payment'),

    # Event
    path('event/add/', views.add_event, name='add_event'),

    # Expenditure
    path('expenditure/add/', views.add_expenditure, name='add_expenditure'),
]
