from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers
from bank_integration.views.item_views import ItemViewSet
from bank_integration.views.payment_views import PaymentViewSet


schema_view = get_schema_view(
    openapi.Info(title="API documentation", default_version='v1.0.0'),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet, basename="Payment")
router.register(r'items', ItemViewSet, basename="Item")

urlpatterns = [
    path('api/', include([
        path('admin/', admin.site.urls),
        path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='api-schema'),
        path('login/', obtain_auth_token, name='generate-token'),
        path('', include(router.urls)),
    ]))
]
