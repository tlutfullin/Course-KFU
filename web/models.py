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


#создание кастомного менеджера
class CustomManager(models.Manager):
    def get_queryset(self):
        # Ваша логика для получения данных из модели
        return super().get_queryset()


#модель классы тексты:
class TextClass(models.Model):
    # Определение собственного менеджера
    objects = models.Manager()

    # поля модели
    id_text = models.AutoField(primary_key = True)
    #id_feature = models.ManyToManyField(FeatureText)
    #title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Исходный текст')
    line_text = models.CharField(max_length=256, verbose_name='Длина текста')
    language_text = models.CharField(max_length=256, verbose_name='Язык')
    style_text = models.CharField(max_length=256, verbose_name='Стиль')
    tone_text = models.CharField(max_length=256, verbose_name='Тон текста')
    informative_value = models.CharField(max_length=256, verbose_name='Исходный текст')
    emotional_coloring = models.CharField(max_length=256, verbose_name='Эмоциональная окраска')
    readability_text = models.CharField(max_length=256, verbose_name='Информативность')
    grammar_text = models.CharField(max_length=256, verbose_name='Грамматика текста')
    syntax_text = models.CharField(max_length=256, verbose_name='Синтаксис текста')
    relevance = models.CharField(max_length=256, verbose_name='Актуальность')
    vocabulary_text =models.CharField(max_length=256, verbose_name='Лексика')
    stylistics_text = models.CharField(max_length=256, verbose_name='Стилистика')
    authorship_text = models.CharField(max_length=256, verbose_name='Авторство')
    lecture_hall = models.CharField(max_length=256, verbose_name='Целевое назначение')
    intended_purpose = models.CharField(max_length=256, verbose_name='Аудитория')
    context_text = models.CharField(max_length=256, verbose_name='Контекст')
    rhythm_text = models.CharField(max_length=256, verbose_name='Ритм текста')
    source_text = models.CharField(max_length=256, verbose_name='Источник')
    impact_text = models.CharField(max_length=256, verbose_name='Воздействие')
    shade_text = models.CharField(max_length=256, verbose_name='Оттенок')
    depth_analysis = models.CharField(max_length=256, verbose_name='Глубина анализа')
    writing_style = models.CharField(max_length=256, verbose_name='Стиль письма')
    main_idea =  models.CharField(max_length=256, verbose_name='Основаня идея текста')

class Action(models.Model):
    id_actions = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(UserWeb, on_delete=models.CASCADE)
    id_text = models.ForeignKey(TextClass, on_delete=models.CASCADE)
    time_session = models.TimeField(auto_now=True)

