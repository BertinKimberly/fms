from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

@login_required(login_url="/users/login/")
def project_list(request):
    project_queryset = Project.objects.all()
    paginator = Paginator(project_queryset, 10)
    page_number = request.GET.get('page', 1)
    projects_page = paginator.get_page(page_number)
    
    return render(request, "projects/project_list.html", {"projects": projects_page})


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project-list")
    else:
        form = ProjectForm()
    return render(request, "projects/project_form.html", {"form": form, "action": "Create"})

def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project-list")
    else:
        form = ProjectForm(instance=project)
    return render(request, "projects/project_form.html", {"form": form, "action": "Update"})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect("project-list")
    return render(request, "projects/project_confirm_delete.html", {"project": project})
