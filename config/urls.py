from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import uuid
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', lambda request: HttpResponse(str(uuid.uuid4()))),
    path('login/', obtain_auth_token, name='generate-token'),
]
