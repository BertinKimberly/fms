from django.db import models
from clients.models import Client
from freelancers.models import Freelancer

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Paid', 'Paid'),
            ('Overdue', 'Overdue')
        ]
    )

    def __str__(self):
        return f'Invoice #{self.id} - {self.client}'
