from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    user = authenticate(request)
    if user:
        return HttpResponse('Ok')
    else:
        return HttpResponse('Usuario o contraseña incorrecto')