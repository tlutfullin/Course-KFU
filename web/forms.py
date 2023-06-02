
from django import forms
from django.contrib.auth import get_user_model

from web.models import TextClass

User = get_user_model()
class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] !=cleaned_data['password2']:
            self.add_error('password', 'Пароли не совпадают')
        return cleaned_data

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())




# class ClassText(forms.ModelForm):
#
#     def save(self, commit=True):
#         self.instance = self.initial['user']
#         super().save(commit)
#     class Meta:
#         model = TextClass
#
#         fields = ('text', 'line_text', 'language_text')
#

class ClassText(forms.ModelForm):
    def save(self, commit=True):
        self.instance = self.initial['user']
        super().save(commit)

    class Meta:
        model = TextClass
        fields = ('text', 'line_text', 'language_text')
        LANGUAGE_CHOICES = [
            ('en', 'English'),
            ('fr', 'French'),
            ('es', 'Spanish'),
            # Добавьте остальные языки, если необходимо
        ]

        LINE_TEXT = [
            ('e', 'короткий'),
            ('ee', 'средней длины'),
            ('df','длинный')
        ]
        widgets = {
            #'text': forms.TextInput(attrs={'class': 'my-autocomplete-widget'}),
            'line_text': forms.Select(choices=LINE_TEXT),
            'language_text': forms.Select(choices=LANGUAGE_CHOICES),
        }











# class ClassText(forms.ModelForm):
#     LANGUAGE_CHOICES = (
#         ('option1', 'Вариант 1'),
#         ('option2', 'Вариант 2'),
#         ('option3', 'Вариант 3'),
#     )
#
#     language_text = forms.MultipleChoiceField(
#         choices=LANGUAGE_CHOICES,
#         widget=forms.CheckboxSelectMultiple
#     )
#
#     class Meta:
#         model = TextClass
#         fields = ('text', 'line_text', 'language_text')
#         # ANSWER_CHOICES = (
#         #     ('option1', 'Вариант 1'),
#         #     ('option2', 'Вариант 2'),
#         #     ('option3', 'Вариант 3'),
#         # )
#         #
#         # answer = forms.ChoiceField(choices=ANSWER_CHOICES, widget=forms.RadioSelect)
#


        
