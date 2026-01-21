from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    position = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    division = models.CharField(max_length=30)
    staffID = models.CharField(max_length=7, unique=True)
    age = models.IntegerField()

    # Contact Information
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    #metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['staffID']

    def __str__(self):
        return self.staffID + '\t' + self.firstname + ' ' + self.lastname

    @property
    def fullname(self):
        return self.firstname + ' ' + self.lastname

    @property
    def full_name(self):
        """Alias for fullname to match template usage"""
        return self.fullname

    