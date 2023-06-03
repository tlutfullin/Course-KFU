# Generated by Django 4.2.1 on 2023-06-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textclass',
            name='authorship_text',
            field=models.CharField(max_length=256, verbose_name='Авторство'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='context_text',
            field=models.CharField(max_length=256, verbose_name='Контекст'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='depth_analysis',
            field=models.CharField(max_length=256, verbose_name='Глубина анализа'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='emotional_coloring',
            field=models.CharField(max_length=256, verbose_name='Эмоциональная окраска'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='grammar_text',
            field=models.CharField(max_length=256, verbose_name='Грамматика текста'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='impact_text',
            field=models.CharField(max_length=256, verbose_name='Воздействие'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='informative_value',
            field=models.CharField(max_length=256, verbose_name='Исходный текст'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='intended_purpose',
            field=models.CharField(max_length=256, verbose_name='Аудитория'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='language_text',
            field=models.CharField(max_length=256, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='lecture_hall',
            field=models.CharField(max_length=256, verbose_name='Целевое назначение'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='line_text',
            field=models.CharField(max_length=256, verbose_name='Длина текста'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='main_idea',
            field=models.CharField(max_length=256, verbose_name='Основаня идея текста'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='readability_text',
            field=models.CharField(max_length=256, verbose_name='Информативность'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='relevance',
            field=models.CharField(max_length=256, verbose_name='Актуальность'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='rhythm_text',
            field=models.CharField(max_length=256, verbose_name='Ритм текста'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='shade_text',
            field=models.CharField(max_length=256, verbose_name='Оттенок'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='source_text',
            field=models.CharField(max_length=256, verbose_name='Источник'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='style_text',
            field=models.CharField(max_length=256, verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='stylistics_text',
            field=models.CharField(max_length=256, verbose_name='Стилистика'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='syntax_text',
            field=models.CharField(max_length=256, verbose_name='Синтаксис текста'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='text',
            field=models.TextField(verbose_name='Исходный текст'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='tone_text',
            field=models.CharField(max_length=256, verbose_name='Тон текста'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='vocabulary_text',
            field=models.CharField(max_length=256, verbose_name='Лексика'),
        ),
        migrations.AlterField(
            model_name='textclass',
            name='writing_style',
            field=models.CharField(max_length=256, verbose_name='Стиль письма'),
        ),
    ]