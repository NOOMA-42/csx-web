from django.shortcuts import render_to_response, redirect, render
from hello.models import game
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def livestream(request):
    ttt = [0, 1, 2]
    if request.method == 'POST':
        #放輸入遊戲的地方 沒有
        return redirect('livestream/')

    if request.method == 'GET':
        return render(request, 'livestream.html', {'ttt': ttt,})

#@csrf_protect
def homepage(request):
    if request.method == 'POST':
        name = request.POST.get('game')
        game.objects.create(name = name)
        listitem = game.objects.all()
        return render(request, 'homepage.html', {"listitem": listitem,})
    if request.method == 'GET':
        listitem = game.objects.all()
        return render(request, 'homepage.html', {"listitem": listitem,})

    