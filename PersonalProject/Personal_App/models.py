from django.db import models
from django.contrib.auth.models import User


class Personal(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE, null=True , blank = True)

    def __str__(self):
        return self.title