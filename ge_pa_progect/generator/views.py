from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')


def description(request):
    return render(request,'generator/description.html')


def password(request):
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
        chars += punctuation

    if request.GET.get('n_simb'):
        chars = str(''.join([i for i in chars if i not in  amb]))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(chars)

    return render(request, 'generator/password.html', {'password':thepassword})