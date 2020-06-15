# I have created this file
import base64
import hashlib

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    data = request.GET.get('text', 'default')
    numbs = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    chrcter = ""
    for char in data:
        if char not in numbs:
            chrcter = chrcter + char
    return HttpResponse(chrcter)


def done(request):
    data = request.POST.get('text', 'default')
    checkmd5=request.POST.get('md5', 'off')
    chkstd=request.POST.get('standard', 'off')
    hsh=""
    Str=""
    if checkmd5=='on':
        en = data.encode()
        h = hashlib.md5(en)
        hsh=h.hexdigest()

    if chkstd=='on':
        Str = base64.b64encode(data.encode('utf-8', errors='strict'))

    prms={'type':'md5', 'done_text': hsh, 'typesd':'standard', 'done_textsd': Str}
    return render(request, 'done.html', prms)
