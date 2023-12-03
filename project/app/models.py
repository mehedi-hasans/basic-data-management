from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media', null=True)
    
    def __str__(self):
      return  self.name
