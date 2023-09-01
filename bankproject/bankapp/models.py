from django.db import models


class Task(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='img')
def __str__(self):
    return self.name
