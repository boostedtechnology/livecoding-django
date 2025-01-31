from django.contrib import admin
from .models import Account, TransactionEntry, Transaction

admin.site.register(Account)
admin.site.register(TransactionEntry)
admin.site.register(Transaction)
