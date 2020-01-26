from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  HttpResponse("hello world")

def about(request):
    return HttpResponse("to jest strona testowa. ʕ•́ᴥ•̀ʔっ")

def cool_text(request, user_text):
    text = 'ʕ•́ᴥ•̀ʔっ' + user_text + 'ʕ•́ᴥ•̀ʔっ'
    return HttpResponse(text)

def name(request, name):
    return render(request, 'example/hello.html'
                  ,{'name': name})



