from rest_framework import viewsets
from bank_integration.models import Item
from bank_integration.serializers.item_serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(payment__owner=self.request.user)
