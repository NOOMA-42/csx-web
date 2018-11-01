from django.shortcuts import redirect, render
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
            return render(request, 'livestream.html', {'ttt': tt,})
        else:
            return render(request, 'homepage.html')
    if request.method == 'GET':
        return render(request, 'homepage.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'homepage.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html',locals())

def logout(request):
	auth.logout(request)  
	return render(request, 'homepage.html')