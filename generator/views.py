from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def homePageView(request):
    lis = [i+1 for i in range(6, 15)]
    return render(request, 'generator/home.html', {'options': lis})


def password(request):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    charactors = list(alphabets)
    length = int(request.GET.get('length',12))

    if request.GET.get("uppercase"):
        charactors.extend(list(alphabets.upper()))

    if request.GET.get("numbers"):
        charactors.extend(list('0123456789'))

    if request.GET.get("special"):
        charactors.extend(list("!@#$%^&*()_+{}\|"))

    the_passord = ''
    for i in range(length):
        the_passord += random.choice(charactors)
    return render(request, 'generator/password.html', {"password": the_passord})
def about(request):
    return render(request,'generator/about.html')