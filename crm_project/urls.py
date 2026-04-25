from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from clients.views import ClientViewSet

def home(request):
    return HttpResponse("<h1>CRM System API</h1><p>Use /api/clients</p>")

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include(router.urls)),
]