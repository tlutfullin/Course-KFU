from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key = True)
    login = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=16, null=False)


class FeatureText(models.Model):
    id_feature = models.AutoField(primary_key = True)
    feature = models.CharField(max_length=500)


class TextClass(models.Model):
    id_text = models.AutoField(primary_key = True)
    id_feature = models.ForeignKey(FeatureText, on_delete=models.CASCADE)
    text = models.TextField()

class Action(models.Model):
    id_actions = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_text = models.ForeignKey(TextClass, on_delete=models.CASCADE)
    time_session = models.TimeField(auto_now=True)

