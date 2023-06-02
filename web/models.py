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


#модель классы тексты:
class TextClass(models.Model):
    id_text = models.AutoField(primary_key = True)
    #id_feature = models.ManyToManyField(FeatureText)
    text = models.TextField()
    line_text = models.CharField(max_length=256)
    language_text = models.CharField(max_length=256)
    style_text = models.CharField(max_length=256)
    tone_text = models.CharField(max_length=256)
    informative_value = models.CharField(max_length=256)
    emotional_coloring = models.CharField(max_length=256)
    readability_text = models.CharField(max_length=256)
    grammar_text = models.CharField(max_length=256)
    syntax_text = models.CharField(max_length=256)
    relevance = models.CharField(max_length=256)
    vocabulary_text =models.CharField(max_length=256)
    stylistics_text = models.CharField(max_length=256)
    authorship_text = models.CharField(max_length=256)
    lecture_hall = models.CharField(max_length=256)
    intended_purpose = models.CharField(max_length=256)
    context_text = models.CharField(max_length=256)
    rhythm_text = models.CharField(max_length=256)
    source_text = models.CharField(max_length=256)
    impact_text = models.CharField(max_length=256)
    shade_text = models.CharField(max_length=256)
    depth_analysis = models.CharField(max_length=256)
    writing_style = models.CharField(max_length=256)
    main_idea =  models.CharField(max_length=256)

class Action(models.Model):
    id_actions = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(UserWeb, on_delete=models.CASCADE)
    id_text = models.ForeignKey(TextClass, on_delete=models.CASCADE)
    time_session = models.TimeField(auto_now=True)

