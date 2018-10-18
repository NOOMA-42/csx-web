from django.shortcuts import render_to_response, redirect
from hello.models import game


# Create your views here.
def livestream(request):
    ttt = [0, 1, 2]
    if request.method == 'POST':
        #放輸入遊戲的地方 沒有
        return redirect('/livestream') 
    return render_to_response('livestream.html',locals())

def homepage(request):
    listitem = game.objects.all()
    return render_to_response('homepage.html', locals())

