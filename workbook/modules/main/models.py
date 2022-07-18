from django.db import models
from django.contrib.auth.models import User

class ListTask(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    description = models.TextField(null=False)
    done = models.BooleanField(null=False, default=False)
    list_task = models.ForeignKey(ListTask, on_delete=models.CASCADE)