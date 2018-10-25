from django.shortcuts import render_to_response, redirect, render
from hello.models import game
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def livestream(request):
    tt = [0, 1, 2]
    return render(request, 'livestream.html', {'ttt': tt,})

def homepage(request):
    tt = [0, 1, 2]
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('livestream/')
        else:
            return render(request, 'homepage.html')
    if request.method == 'GET':
        return render(request, 'homepage.html', {'ttt': tt,})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',locals())

def logout(request):
	auth.logout(request)  
	return redirect('')