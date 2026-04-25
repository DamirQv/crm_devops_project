from rest_framework import viewsets, filters
from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer
import logging

logger = logging.getLogger(__name__)

def clients_page(request):
    logger.info("Clients page opened")

# API
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


# HTML страница
def clients_page(request):
    query = request.GET.get('q')

    if query:
        clients = Client.objects.filter(name__icontains=query)
    else:
        clients = Client.objects.all()

    return render(request, 'clients.html', {'clients': clients})