from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Account, Transaction, TransactionEntry

class Task3TestsCase(APITestCase):
    def setUp(self):
        self.asset_account = Account.objects.create(name='Bank (TD Canada Trust)', type='ASSET')
        self.liability_account = Account.objects.create(name='Credit Card', type='LIABILITY')
        self.expense_account = Account.objects.create(name='Office Supplies', type='EXPENSE')
        self.revenue_account = Account.objects.create(name='Revenue', type='REVENUE')

        self.expense_transaction = Transaction.objects.create(description='Valid Transaction')
        TransactionEntry.objects.create(account=self.asset_account, type='CREDIT', amount=10, transaction=self.expense_transaction)
        TransactionEntry.objects.create(account=self.liability_account, type='CREDIT', amount=10, transaction=self.expense_transaction)
        TransactionEntry.objects.create(account=self.expense_account, type='DEBIT', amount=20, transaction=self.expense_transaction)

        self.revenue_transaction = Transaction.objects.create(description='Valid Transaction')
        TransactionEntry.objects.create(account=self.asset_account, type='DEBIT', amount=800, transaction=self.revenue_transaction)
        TransactionEntry.objects.create(account=self.revenue_account, type='CREDIT', amount=800, transaction=self.revenue_transaction)

    def test_get_asset_account_balance(self):
        response = self.client.get(reverse('account-retrieve-update-destroy', args=[self.asset_account.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], 790)

    def test_get_expense_account_balance(self):
        response = self.client.get(reverse('account-retrieve-update-destroy', args=[self.expense_account.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], 20)
