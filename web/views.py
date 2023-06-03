import gensim
import joblib
import numpy as np
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm, TextClass, ClassTextForm, TextInputForm

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import pymorphy2
import ufal.udpipe as udp
import corpy.udpipe as crp


stop_words = set(stopwords.words('russian'))
nltk_tokenizer = RegexpTokenizer(r'[а-яёa-z]+')

morph = pymorphy2.MorphAnalyzer()


User = get_user_model()



# def main_view(request):
#     classtexts = TextClass.objects.all()
#     return render(request, 'web/main.html', {'classtexts':classtexts})

def text_preprocessing(text):
    words = nltk_tokenizer.tokenize(text.lower())
    lem_text = [morph.parse(w)[0].normal_form for w in words if w not in stop_words]

    return lem_text



# Загрузка модели в оболочку corpy
corpy_model = crp.Model('russian-syntagrus-ud-2.5-191206.udpipe')
# Функция для тегирования слов

def udp_tagging(lem_text):
    sents = [list(corpy_model.process(w)) for w in lem_text]
    tagged_words = [s[0].words[1].form + '_' + s[0].words[1].upostag for s in sents if s]

    return tagged_words



def main_view(request):

    # def predict_category(text):
    #     # Загрузка сохраненной модели
    #     loaded_model = joblib.load('model.pkl')
    #
    #     predictions = loaded_model.predict(new_data)
    #     return predictions

    category = None
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            loaded_model = joblib.load('model.pkl')
            text = form.cleaned_data['text_field']

            fake_preproc = udp_tagging(text_preprocessing(text))
            w2v = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

            fake_words_tagged = []
            for word in fake_preproc:
                if word in w2v.vocab:
                    fake_words_tagged.append(word)

            fake_indexed = np.array(list(map(lambda x: w2v.vocab[x].index, fake_words_tagged))).astype('float32')

            category = loaded_model.predict(fake_indexed)

    else:
        form = TextInputForm()

    return render(request, 'web/main.html', {'form': form, 'category': category})


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            user = User(username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'])

            user.set_password(form.cleaned_data["password"])
            user.save()

            is_success = True
    return  render(request, 'web/registration.html',
                   {'form': form, 'is_success': is_success})


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введен неправильный логин или пароль")
            else:
                login(request, user)
                return redirect('main')
    return render(request, 'web/auth.html', {'form': form })



def logout_view(request):
    logout(request)
    return redirect('main')

def history_view(request):
    classtexts = TextClass.objects.all()
    return render(request, 'web/history.html', {'classtexts': classtexts})

def class_text_edit_view(request, id=None):

    # из модели(таблицы) достаем данные, если id непустой то возвращаем None
    class_text = TextClass.objects.get(id_text=id) if id is not None else None
    # иницилизируем форму
    form = ClassTextForm(instance=class_text)
    if request.method=='POST':
        form = ClassTextForm(data = request.POST,instance=class_text, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('main')

    return render(request, 'web/class_text.html', {'form': form})



# def text_prediction_view(request):
#     if request.method == 'POST':
#         form = TextInputForm(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text_field']
#             # category = predict_category(text)
#             # return render(request, 'prediction_result.html', {'category': category})
#             return render(request, 'prediction_result.html', {'category': text})
#     else:
#         form = TextInputForm()
#
#     return render(request, 'text_prediction.html', {'form': form})
#





# def class_text_edit_view(request, id=None):
#     class_text = TextClass.objects.get(id=id) if id is not None else None
#
#     if request.method == 'POST':
#         form = ClassTextForm(data=request.POST, instance=class_text, initial={'user': request.user})
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     else:
#         form = ClassTextForm(instance=class_text)
#
#     return render(request, 'web/class_text.html', {'form': form})