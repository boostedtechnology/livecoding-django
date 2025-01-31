from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/<uuid:pk>/', views.AccountRetrieveUpdateDestroyView.as_view(), name='account-retrieve-update-destroy'),
    # path('transactions/', views.TransactionCreateView.as_view(), name='transaction-create'),
] 