from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    #return render(request,"/polls/index.html",context)
    return HttpResponse(request,)