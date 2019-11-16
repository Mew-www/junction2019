from rest_framework import viewsets
from bank_integration.serializers.payment_serializer import PaymentSerializer
from bank_integration.models import Payment
from rest_framework.decorators import action
from rest_framework.response import Response
import json


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(owner=self.request.user)

    @action(methods=['post'], detail=False, url_path='import')
    def import_data(self, request):
        for serializer in [PaymentSerializer(data=entity) for entity in json.loads(request.body)]:
            if serializer.is_valid():
                serializer.save(owner=request.user)
            else:
                return Response(status=400, data=serializer.errors)
        return Response(status=201)
