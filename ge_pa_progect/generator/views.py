from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    password = 'Нажми кнопку сгенерировать пароль'
    return render(request, 'generator/home.html', {'password': password})


def generate_password(request):
    digits = '0123456789'
    lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    punctuation = '!#$%&*+-=?@^_'
    chars = lowercase_letters
    amb = 'il1Lo0O'

    length = int(request.GET.get('length', 8))

    if request.GET.get('uppercase'):
        chars += uppercase_letters

    if request.GET.get('numbers'):
        chars += digits

    if request.GET.get('special'):
        # print(request.GET.get('special'))
        chars += punctuation

    if request.GET.get('n_simb'):
        chars = str(''.join([i for i in chars if i not in amb]))

    password = ''
    for i in range(length):
        password += random.choice(chars)

    return render(request, 'generator/home.html', {'password': password})
