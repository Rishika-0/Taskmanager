from django.db import models

# Create your models here.

class Task(models.Model):
    uname=models.CharField(max_length=100)
    title=models.CharField(max_length=400)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class data(models.Model):
    
    uname=models.CharField(max_length=20)
    passw=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
