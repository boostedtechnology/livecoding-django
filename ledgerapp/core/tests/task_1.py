from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Account
import uuid

class Task1TestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Test account record
        self.account_data = {'name': 'Inventory', 'type': 'LIABILITY'}
        self.account = Account.objects.create(**self.account_data)

        self.detail_url = reverse('account-retrieve-update-destroy', kwargs={'pk': self.account.pk})

    def test_delete_account(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Account.objects.count(), 0)

