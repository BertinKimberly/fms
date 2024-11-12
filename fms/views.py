from django.shortcuts import render
from clients.models import Client
from freelancers.models import Freelancer
from projects.models import Project
from users.models import CustomUser
from django.db.models import Avg, Count
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login")
def homepage(request):
     total_projects = Project.objects.count()
     total_clients = Client.objects.count()
     total_users = CustomUser.objects.count()
     total_freelancers = Freelancer.objects.count()
     
     recent_projects = Project.objects.order_by('-id')[:10]
     avg_project_budget = Project.objects.aggregate(Avg('budget'))['budget__avg']
     avg_freelancer_rate = Freelancer.objects.aggregate(Avg('hourly_rate'))['hourly_rate__avg']
     project_field_distribution = Project.objects.values('field').annotate(count=Count('field')).order_by('-count')

     context = {
        'total_projects': total_projects,
        'total_clients': total_clients,
        'total_users': total_users,
        'total_freelancers': total_freelancers,
        'recent_projects': recent_projects,
        'avg_project_budget': avg_project_budget,
        'avg_freelancer_rate': avg_freelancer_rate,
        'project_field_distribution': {entry['field']: entry['count'] for entry in project_field_distribution},
     }
     return render(request, 'home.html', context)