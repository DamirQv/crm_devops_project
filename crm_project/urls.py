from django.contrib import admin
from django.urls import path, include
from crm_project.views import home
from rest_framework.routers import DefaultRouter
from clients.views import ClientViewSet
from clients.views import clients_page
from accounts.views import register_view, login_view, logout_view

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include('clients.urls')),
    path('clients/', clients_page),
]

urlpatterns += [
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
]