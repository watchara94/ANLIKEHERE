from django.db import models
from datetime import datetime    
from django.utils import timezone

class refridgerator_display_system(models.Model):
    name = models.TextField(default="")
    id = models.TextField(primary_key=True)
    datetime_regis = models.DateTimeField(default=timezone.now())

class history(models.Model):
    ref_id = models.ForeignKey(refridgerator_display_system,on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())