from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(u"安安 游祖鈞到此一遊")
