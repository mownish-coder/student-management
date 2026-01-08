from django.db import models

class details(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name
# 

# Create your models here.
