from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.

class UserWeb(models.Model):
    id_user = models.AutoField(primary_key = True)
    login = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=16, null=False)


class FeatureText(models.Model):
    id_feature = models.AutoField(primary_key = True)
    feature = models.CharField(max_length=500)


class TextClass(models.Model):
    id_text = models.AutoField(primary_key = True)
    id_feature = models.ManyToManyField(FeatureText)
    text = models.TextField()

class Action(models.Model):
    id_actions = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(UserWeb, on_delete=models.CASCADE)
    id_text = models.ForeignKey(TextClass, on_delete=models.CASCADE)
    time_session = models.TimeField(auto_now=True)

