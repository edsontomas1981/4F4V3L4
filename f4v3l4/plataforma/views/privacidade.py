from django.shortcuts import render,redirect


def privacidade(request):
    if request.method == "GET" :
        return render(request,'./privacidade.html')
    elif request.method == 'POST':
        return render (request,'./privacidade.html')