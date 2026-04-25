from django.shortcuts import render
from clients.models import Client

def home(request):
    clients = Client.objects.all().order_by('-created_at')[:5]
    total_clients = Client.objects.count()

    context = {
        'clients': clients,
        'total_clients': total_clients,
    }

    return render(request, 'home.html', context)