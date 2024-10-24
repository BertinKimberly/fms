from django.db import models

class Project(models.Model):
    FIELDS=[
        ('Transport','Transport'),
        ('Agriculture','Agriculture'),
        ('Trade','Trade'),
        ('Environmental Protection','Environmental Protection'),
    ]
    name=models.CharField(max_length=255)
    field=models.CharField(max_length=255,choices=FIELDS)
    description=models.TextField(max_length=1000)
    budget=models.IntegerField()

    
    def __str__(self):
        return self.name
    
    class Meta:
       db_table="projects"