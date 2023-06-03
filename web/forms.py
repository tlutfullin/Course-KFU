from django import forms
from django.contrib.auth import get_user_model

from web.models import TextClass

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', 'Пароли не совпадают')
        return cleaned_data

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


# class ClassTextForm(forms.ModelForm):
#
#     # def save(self, commit=True):
#     #     self.instance = self.initial['tone_text']
#     #     super().save(commit)
#
#     class Meta:
#         model = TextClass
#
#         fields = ('text', 'line_text', 'language_text', 'informative_value')

class ClassTextForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)
    class Meta:
        model = TextClass
        fields = ('text', 'line_text', 'language_text', 'style_text', 'tone_text', 'informative_value',
                  'emotional_coloring', 'readability_text', 'grammar_text', 'syntax_text', 'relevance',
                  'vocabulary_text', 'stylistics_text', 'authorship_text', 'lecture_hall', 'intended_purpose',
                  'context_text', 'rhythm_text', 'source_text', 'impact_text', 'shade_text', 'depth_analysis',
                  'writing_style', 'main_idea')


        LANGUAEGE_TEXT = [
            ('English', 'Английский'),
            ('Russian', 'Русский'),
            ('Russian', 'Испанский'),
            ('French', 'Французский'),
        ]

        LINE_TEXT = [
            ('short', 'Короткий'),
            ('medium', 'Средней длины'),
            ('long', 'Длинный'),
        ]

        STYLE_TEXT = [
            ('formal', 'Формальный'),
            ('informal', 'Неформальный'),
            ('academic', 'Академический'),
            ('poetic', 'Поэтический'),
        ]

        TONE_TEXT = [
            ('serious', 'Серьезный'),
            ('humorous', 'Шуточный'),
            ('emotional', 'Эмоциональный'),
            ('informative', 'Информативный'),
        ]

        INFORMATIVE_VALUE = [
            ('informative', 'Содержательный'),
            ('superficial', 'Поверхностный'),
            ('detailed', 'Подробный'),
        ]

        EMOTIONAL_COLORING = [
            ('joyful', 'Радостный'),
            ('sad', 'Грустный'),
            ('disappointed', 'Разочарованный'),
        ]

        READABILITY_TEXT = [
            ('easy', 'Легко читаемый'),
            ('difficult', 'Трудно читаемый'),
            ('legible', 'Разборчивый'),
        ]

        GRAMMAR_TEXT = [
            ('correct', 'Правильная'),
            ('incorrect', 'Неправильная'),
            ('with_errors', 'С ошибками'),
        ]

        SYNTAX_TEXT = [
            ('simple', 'Простой'),
            ('complex', 'Сложный'),
            ('indented', 'С отступлениями'),
        ]

        RELEVANCE = [
            ('current', 'Актуальный'),
            ('outdated', 'Устаревший'),
            ('modern', 'Современный'),
        ]

        VOCABULARY_TEXT = [
            ('specialized', 'Специализированная'),
            ('complex', 'Сложная'),
            ('simple', 'Простая'),
            ('technical', 'Техническая'),
        ]

        STYLISTICS_TEXT = [
            ('official', 'Официальный'),
            ('scientific', 'Научный'),
            ('business', 'Деловой'),
            ('artistic', 'Художественный'),
        ]

        AUTHORSHIP_TEXT = [
            ('original', 'Авторский текст'),
            ('quotation', 'Цитата'),
            ('anonymous', 'Анонимный текст'),
        ]

        RICHNESS_CHOICES = [
            ('rich', 'Насыщенный'),
            ('sparse', 'Скудный'),
            ('informative', 'Информативный'),
        ]

        SENSITIVITY_CHOICES = [
            ('sensitive', 'Чувствительный'),
            ('neutral', 'Нейтральный'),
            ('emotional', 'Эмоциональный'),
        ]

        INTENDED_PURPOSE = [
            ('scientific', 'Научный текст'),
            ('children', 'Детский текст'),
            ('specialized', 'Специализированный текст'),
        ]

        LECTURE_HALL = [
            ('informational', 'Информационный'),
            ('entertainment', 'Развлекательный'),
            ('journalistic', 'Публицистический'),
        ]

        CONTEXT_TEXT = [
            ('social', 'Социальный'),
            ('political', 'Политический'),
            ('cultural', 'Культурный'),
            ('historical', 'Исторический'),
        ]

        SPECIFICITY_CHOICES = [
            ('scientific', 'Научный текст'),
            ('news', 'Новостной текст'),
            ('legal', 'Юридический текст'),
            ('artistic', 'Художественный текст'),
        ]

        RHYTHM_TEXT = [
            ('rhythmic', 'Ритмичный'),
            ('non-rhythmic', 'Неритмичный'),
            ('monotonous', 'Монотонный'),
        ]

        INFORMATIVE_CHOICES = [
            ('informative', 'Информативный'),
            ('inaccurate', 'Неточный'),
            ('complete', 'Полный'),
            ('incomplete', 'Неполный'),
        ]

        TONE_CHOICES = [
            ('formal', 'Формальный'),
            ('informal', 'Неформальный'),
            ('ironic', 'Ироничный'),
            ('sarcastic', 'Саркастический'),
        ]

        SOURCE_TEXT = [
            ('original', 'Оригинальный текст'),
            ('translation', 'Перевод'),
            ('quotation', 'Цитата'),
        ]

        IMPACT_TEXT = [
            ('convincing', 'Убедительный'),
            ('emotional', 'Эмоциональный'),
            ('positive', 'Позитивный'),
            ('negative', 'Негативный'),
        ]

        SHADE_TEXT = [
            ('neutral', 'Нейтральный'),
            ('positive', 'Позитивный'),
            ('negative', 'Негативный'),
        ]

        DEPTH_ANALYSIS = [
            ('superficial', 'Поверхностный'),
            ('deep', 'Глубокий'),
            ('detailed', 'Детальный'),
        ]

        COHERENCE_CHOICES = [
            ('coherent', 'Связный'),
            ('disjointed', 'Разрозненный'),
            ('sequential', 'Последовательный'),
        ]

        WRITING_STYLE = [
            ('epistolary', 'Эпистолярный'),
            ('business', 'Деловой'),
            ('creative', 'Креативный'),
        ]

        CONTRAST_CHOICES = [
            ('contrasting', 'Контрастный'),
            ('uniform', 'Однообразный'),
            ('monochrome', 'Монохромный'),
        ]

        ACTIVITY_CHOICES = [
            ('active', 'Активный'),
            ('passive', 'Пассивный'),
            ('neutral', 'Нейтральный'),
        ]

        MAIN_IDEA = [
            ('clear', 'Ясная'),
            ('unclear', 'Неясная'),
            ('ambiguous', 'Неоднозначная'),
        ]

        widgets = {
            'language_text': forms.Select(choices=LANGUAEGE_TEXT),
            'line_text': forms.Select(choices=LINE_TEXT),
            'style_text': forms.Select(choices=STYLE_TEXT),
            'tone_text': forms.Select(choices=TONE_TEXT),
            'informative_value': forms.Select(choices=INFORMATIVE_VALUE),
            'emotional_coloring': forms.Select(choices=EMOTIONAL_COLORING),
            'readability_text': forms.Select(choices=READABILITY_TEXT),
            'grammar_text': forms.Select(choices=GRAMMAR_TEXT),
            'syntax_text': forms.Select(choices=SYNTAX_TEXT),
            'relevance': forms.Select(choices=RELEVANCE),
            'vocabulary_text': forms.Select(choices=VOCABULARY_TEXT),
            'stylistics_text': forms.Select(choices=STYLISTICS_TEXT),
            'authorship_text': forms.Select(choices=AUTHORSHIP_TEXT),
            'lecture_hall': forms.Select(choices=LECTURE_HALL),
            'intended_purpose': forms.Select(choices=INTENDED_PURPOSE),
            'context_text': forms.Select(choices=CONTEXT_TEXT),
            'rhythm_text': forms.Select(choices=RHYTHM_TEXT),
            'source_text': forms.Select(choices=SOURCE_TEXT),
            'impact_text': forms.Select(choices=IMPACT_TEXT),
            'shade_text': forms.Select(choices=SHADE_TEXT),
            'depth_analysis': forms.Select(choices=DEPTH_ANALYSIS),
            'writing_style': forms.Select(choices=WRITING_STYLE),
            'main_idea': forms.Select(choices=MAIN_IDEA),
        }

class TextInputForm(forms.Form):
    text_field = forms.CharField(label='Введите  заголовок')
    text_heading = forms.CharField(label='Введите текст', widget=forms.Textarea)




# Длина: короткий, средней длины, длинный.
# Ширина: узкий, средней ширины, широкий.
# Размер: маленький, средний, большой.
# Шрифт: курсивный, жирный, обычный, заглавный.
# Стиль: формальный, неформальный, академический, поэтический.
# Тон: серьезный, шуточный, эмоциональный, информативный.
# Цвет: черный, белый, красный, синий и т.д.
# Информативность: содержательный, поверхностный, подробный.
# Эмоциональная окраска: радостный, грустный, разочарованный.
# Технические особенности: кодировка, разметка, ссылки, заголовки.
# Читабельность: легко читаемый, трудно читаемый, разборчивый.
# Структура: параграфы, списки, заголовки, подзаголовки.
# Грамматика: правильная, неправильная, с ошибками.
# Синтаксис: простой, сложный, с отступлениями.
# Актуальность: актуальный, устаревший, современный.


# Форматирование: выравнивание по левому краю, по правому краю, по центру, по ширине.
# Язык: английский, русский, испанский, французский и т.д.
# Лексика: специализированная, сложная, простая, техническая.
# Стилистика: официальный, научный, деловой, художественный.
# Ориентация: горизонтальный, вертикальный.
# Авторство: авторский текст, цитата, анонимный текст.
# Насыщенность: насыщенный, скудный, информативный.
# Акцент: основной акцент, второстепенный акцент.
# Чувствительность: чувствительный, нейтральный, эмоциональный.
# Аудитория: научный текст, детский текст, специализированный текст.
# Целевое назначение: информационный, развлекательный, публицистический.
# Сложность: простой, сложный, понятный, непонятный.
# Актуальность: актуальный, устаревший, текущий.
# Контекст: социальный, политический, культурный, исторический.
# Специфика: научный текст, новостной текст, юридический текст, художественный текст.


# Ритм: ритмичный, неритмичный, монотонный.
# Информативность: информативный, неточный, полный, неполный.
# Тон: формальный, неформальный, ироничный, саркастический.
# Источник: оригинальный текст, перевод, цитата.
# Воздействие: убедительный, эмоциональный, позитивный, негативный.
# Оттенок: нейтральный, позитивный, негативный, нейтральный.
# Временные рамки: прошедший, настоящий, будущий.
# Глубина анализа: поверхностный, глубокий, детальный.
# Связность: связный, разрозненный, последовательный.
# Сочетаемость: хорошо сочетаемый, несочетаемый, контрастный.
# Конкретность: конкретный, абстрактный, образный.
# Стиль письма: эпистолярный, деловой, креативный.
# Контрастность: контрастный, однообразный, монохромный.
# Активность: активный, пассивный, нейтральный.
# Основная идея: ясная, неясная, неоднозначная.

