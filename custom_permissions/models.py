from django.db import models

# Create your models here.

class Cars(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    m_no = models.CharField(max_length=100)
