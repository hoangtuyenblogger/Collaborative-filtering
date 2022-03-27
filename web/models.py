from django.db import models

# Create your models here.

class employer(models.Model):
    name = models.CharField(max_length=100)
    job_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    ex = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class jobs(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    salary = models.CharField(max_length=20)
    ex = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_name = models.CharField(max_length=200)
    def __str__(self):
        return self.title