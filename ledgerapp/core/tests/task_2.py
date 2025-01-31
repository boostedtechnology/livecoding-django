from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Account

class TransactionTests(APITestCase):
    def setUp(self):
        self.asset_account = Account.objects.create(name='Bank (TD Canada Trust)', type='ASSET')
        self.liability_account = Account.objects.create(name='Credit Card', type='LIABILITY')
        self.expense_account = Account.objects.create(name='Office Supplies', type='EXPENSE')

    def test_create_valid_transaction(self):
        transaction_data = {
            'description': 'Valid Transaction',
            'entries': [
                {'account': self.asset_account.pk, 'type': 'CREDIT', 'amount': 5500},
                {'account': self.liability_account.pk, 'type': 'CREDIT', 'amount': 2200},
                {'account': self.expense_account.pk, 'type': 'DEBIT', 'amount': 7700},
            ]
        }
        response = self.client.post(reverse('transaction-create'), transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_transaction_debits_credits_not_equal(self):
        transaction_data = {
            'description': 'Invalid Transaction',
            'entries': [
                {'account': self.asset_account.pk, 'type': 'DEBIT', 'amount': 100},
                {'account': self.liability_account.pk, 'type': 'CREDIT', 'amount': 30},
            ]
        }
        response = self.client.post(reverse('transaction-create'), transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Total debits and credits must be equal.', str(response.data))

    def test_create_transaction_no_entries(self):
        transaction_data = {
            'description': 'No Entries Transaction',
            'entries': []
        }
        response = self.client.post(reverse('transaction-create'), transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('There must be at least two entries.', str(response.data))

    def test_create_transaction_with_negative_amount(self):
        transaction_data = {
            'description': 'Negative Amount Transaction',
            'entries': [
                {'account': self.asset_account.pk, 'type': 'CREDIT', 'amount': -5500},
                {'account': self.expense_account.pk, 'type': 'DEBIT', 'amount': -5500},
            ]
        }
        response = self.client.post(reverse('transaction-create'), transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Amount cannot be less than 0.', str(response.data))

    def test_create_transaction_with_same_account_twice(self):
        transaction_data = {
            'description': 'Same Account Twice Transaction',
            'entries': [
                {'account': self.asset_account.pk, 'type': 'CREDIT', 'amount': 5500},
                {'account': self.asset_account.pk, 'type': 'DEBIT', 'amount': 5500},
            ]
        }
