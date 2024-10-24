from django.db import models
from projects.models import Project


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)  
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name