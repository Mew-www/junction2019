from django.db import models
from django.conf import settings
import uuid


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount_sents = models.IntegerField()
    store = models.CharField(max_length=255)


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price_sents = models.IntegerField()
    rating = models.IntegerField()
