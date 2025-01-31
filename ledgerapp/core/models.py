from django.db import models
import uuid

class Account(models.Model):
    class AccountType(models.TextChoices):
        ASSET = 'ASSET', 'Asset'
        LIABILITY = 'LIABILITY', 'Liability'
        EQUITY = 'EQUITY', 'Equity'
        REVENUE = 'REVENUE', 'Revenue'
        EXPENSE = 'EXPENSE', 'Expense'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=AccountType.choices)


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)


class TransactionEntry(models.Model):
    class TransactionEntryType(models.TextChoices):
        DEBIT = 'DEBIT', 'Debit'
        CREDIT = 'CREDIT', 'Credit'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='entries')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='entries')
    amount = models.BigIntegerField()
    type = models.CharField(max_length=10, choices=TransactionEntryType.choices)