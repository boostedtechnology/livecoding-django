from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer
from django.http import Http404

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# AccountRetrieveUpdateDestroyView is a view that, after completing task 1, should be
# able to retrieve, update, and delete an account model.
# 
# When implementing Task 1, you can use either:
# 1. Inherit the correct Django REST Framework Generic view(s) (https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)
# or
# 2. Implement the `delete` method manually
class AccountRetrieveUpdateDestroyView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # PUT request to update an account
    def put(self, request, *args, **kwargs):
        account = Account.objects.filter(id=kwargs["pk"])
        if not account.exists():
            return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(account.first(), data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class TransactionCreateView():
    pass
