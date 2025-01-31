from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Account
import uuid

class AccountAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Test account record
        self.account_data = {'name': 'Inventory', 'type': 'ASSET'}
        self.account = Account.objects.create(**self.account_data)

        self.list_create_url = reverse('account-list-create')
        self.detail_url = reverse('account-retrieve-update-destroy', kwargs={'pk': self.account.pk})

    def test_create_account(self):
        count_before = Account.objects.count()
        response = self.client.post(self.list_create_url, {'name': 'Accounts Payable', 'type': 'LIABILITY'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), count_before + 1)

    def test_create_account_without_name(self):
        response = self.client.post(self.list_create_url, {'type': 'EQUITY'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)  # Checks if 'name' field is mentioned in the error

    def test_retrieve_account(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.account_data['name'])

    def test_update_account(self):
        response = self.client.put(self.detail_url, {'name': 'Owner\'s Equity', 'type': 'EQUITY'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.assertEqual(self.account.name, 'Owner\'s Equity')

    def test_update_nonexistent_account(self):
        # Create a new URL for a non-existent account
        non_existent_id = uuid.uuid4()
        detail_url_for_nonexistent = reverse('account-retrieve-update-destroy', kwargs={'pk': non_existent_id})
        response = self.client.put(detail_url_for_nonexistent, {'name': 'Nonexistent Account', 'type': 'EQUITY'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
