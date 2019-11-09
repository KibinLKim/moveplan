from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def features(request):
    return render(request,'features.html')

# Home
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def portfolio(request):
    return render(request,'portfolio.html')

def registration(request):
    return render(request,'registration.html')