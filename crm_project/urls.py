from django.contrib import admin
from django.urls import path, include
from crm_project.views import home
from rest_framework.routers import DefaultRouter
from clients.views import ClientViewSet
from clients.views import clients_page

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include(router.urls)),
    path('clients/', clients_page),
]