from django.db import models

# Create your models here.

status_list = (
    ('normal','normal'),
    ("warning",'warning'),
    ("alert","alert")
)

class TemperatureLog(models.Model):
    lake = models.CharField(max_length=200, null=True, blank=True)
    temperature =  models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(auto_now=True,auto_created=True)
    region =  models.CharField(max_length=200, null=True, blank=True)
    status =  models.CharField(max_length=200, choices=status_list,null=True, blank=True)
    depth = models.CharField(max_length=200,null=True)


