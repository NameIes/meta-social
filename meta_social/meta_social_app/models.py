from django.contrib.auth.models import User
from django.db import models

class LoginAttempt(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    capcha = models.CharField(max_length=50)
    ok = models.BooleanField()
