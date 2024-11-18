from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
         ('Freelancer', 'Freelancer'),
        ('Client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
    )

    def __str__(self):
        return self.username
    
    class Meta:
        db_table="users"