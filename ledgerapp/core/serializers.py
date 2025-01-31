from rest_framework import serializers
from .models import Account, Transaction, TransactionEntry
from django.db.models import Sum, F, Case, When

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'type']

class TransactionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionEntry
        fields = ['account', 'type', 'amount']

class TransactionSerializer(serializers.ModelSerializer):
    entries = TransactionEntrySerializer(many=True)

    class Meta:
        model = Transaction
        fields = ['description', 'entries']

    # You may or may not want to implement these

    def validate_entries(self, entries):
        pass

    def validate(self, data):
        pass

    def create(self, validated_data):
        pass