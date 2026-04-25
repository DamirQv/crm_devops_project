from clients.models import Client
from deals.models import Deal
from tasks.models import Task
from django.shortcuts import render

def home(request):
    total_clients = Client.objects.count()
    total_deals = Deal.objects.count()
    total_tasks = Task.objects.count()

    clients = Client.objects.all().order_by('-created_at')[:5]

    context = {
        'total_clients': total_clients,
        'total_deals': total_deals,
        'total_tasks': total_tasks,
        'clients': clients,
    }

    return render(request, 'home.html', context)