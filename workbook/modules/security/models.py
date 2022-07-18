from django.db import models
from django.contrib.auth.models import User

from modules.security.methods import get_file_path


class Profile(models.Model):
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Color(models.Model):
    primary_color = models.CharField(
        max_length=10, default='#6aa5ff', null=False)
    primary_trans_color = models.CharField(
        max_length=10, default='#6aa5ff77', null=False)
    secondary_color = models.CharField(
        max_length=10, default='#4883dd', null=False)
    base_color = models.CharField(max_length=10, default='#fff', null=False)
    base_trans_color = models.CharField(max_length=10, default='#fff7', null=False)
    text_color = models.CharField(max_length=10, default='#000', null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
