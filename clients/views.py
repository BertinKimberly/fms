from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from django.core.paginator import Paginator
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login/")
def client_list(request):
    client_queryset = Client.objects.all()
    paginator = Paginator(client_queryset, 10)
    page_number = request.GET.get('page', 1)
    clients_page = paginator.get_page(page_number)
    
    return render(request, "clients/client_list.html", {"clients": clients_page})


def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client-list")
    else:
        form = ClientForm()
    return render(request, "clients/client_form.html", {"form": form, "action": "Create"})

def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client-list")
    else:
        form = ClientForm(instance=client)
    return render(request, "clients/client_form.html", {"form": form, "action": "Update"})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect("client-list")
    return render(request, "clients/client_confirm_delete.html", {"client": client})
