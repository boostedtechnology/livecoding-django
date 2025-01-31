from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionCreateView():
    pass
