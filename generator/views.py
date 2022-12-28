from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list("abcdefghijklmnoprstuvwz")

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIKLMNOPRSTUVWZ'))
    
    if request.GET.get('spcharacter'):
        characters.extend(list('!@#$%&*'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length'))
    password = ''
    
    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, 'generator/about.html')