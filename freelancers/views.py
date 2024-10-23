from django.shortcuts import render, get_object_or_404, redirect
from .models import Freelancer
from .forms import FreelancerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login/")
def freelancer_list(request):
    freelancer_queryset = Freelancer.objects.all()
    

    paginator = Paginator(freelancer_queryset, 10)
    
    page_number = request.GET.get('page', 1)
    
   
    freelancers_page = paginator.get_page(page_number)
    
    return render(request, "freelancers/freelancer_list.html", {"freelancers": freelancers_page})

def create_freelancer(request):
    if request.method == "POST":
        form = FreelancerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../")
    else:
        form = FreelancerForm()
    return render(request, "freelancers/freelancer_form.html", {"form": form, "action": "Create"})

def update_freelancer(request, pk):
    freelancer = get_object_or_404(Freelancer, pk=pk)
    if request.method == "POST":
        form = FreelancerForm(request.POST, instance=freelancer)
        if form.is_valid():
            form.save()
            return redirect("freelancer_list")
    else:
        form = FreelancerForm(instance=freelancer)
    return render(request, "freelancers/freelancer_form.html", {"form": form, "action": "Update"})

def delete_freelancer(request, pk):
    freelancer = get_object_or_404(Freelancer, pk=pk)
    if request.method == "POST":
        freelancer.delete()
        return redirect("freelancer-list")
    return render(request, "freelancers/freelancer_confirm_delete.html", {"freelancer": freelancer})
