from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'about.html')

def funding(request):
    return render(request,'funding.html')

def history(request):
    return render(request,'history.html')

# Home
def index(request):
    return render(request,'index.html')




