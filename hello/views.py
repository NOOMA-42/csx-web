from django.shortcuts import render
from hello.models import Account


# Create your views here.
def index(request):
    ttt = [0, 1, 2]
    return render(request, 'hw1.html',locals())
