from rest_framework import viewsets, filters
from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer

# API (для /api/clients/)
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


# UI страница (/clients/)
def clients_page(request):
    query = request.GET.get('q')

    if query:
        clients = Client.objects.filter(name__icontains=query)
    else:
        clients = Client.objects.all()

    return render(request, 'clients.html', {'clients': clients})