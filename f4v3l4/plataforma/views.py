from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/auth/login/')
def home(request):
    if request.method == "GET" : 
        return render(request,'./home.html')
    elif request.method == "POST" :
        return render(request,'./home.html')