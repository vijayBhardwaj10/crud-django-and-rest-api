from django.db import models

# Create your models here.
class employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code =models.CharField(max_length=3)
    mob =models.CharField(max_length=15)


    #Create /Insert /Add - Post
    #Retrieve /Fetch - Get
    #Update /Edit - Put
    #Delete /Remove -Delete