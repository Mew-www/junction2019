from django.contrib import admin
from bank_integration.models import Payment, Item

admin.site.register(Payment)
admin.site.register(Item)
