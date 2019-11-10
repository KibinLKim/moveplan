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

    
def ExpectedRevenue(request):
  ThreeMonthCost = request.GET['ThreeMonthCost']
  YearPerformance = request.GET['YearPerformance']
  YearAllowance = request.GET['YearAllowance']
  Workdays = request.GET['Workdays']
  if request.method == 'POST':   
      Revenue = (ThreeMonthCost+YearPerformance*3/12 + YearAllowance*3/12)
      Revenue2 = Revenue/90*30*(Workdays/365)
      RetireExpected = Revenue2
      return render(request, '',{'RetireExpected': RetireExpected})

def PrivacyPension(request):
  InvestmentPay = request.GET['InvestmentPay']
  PensionRateReturn = request.GET['PensionRateReturn']
  MonthCompound = request.GET['MonthCompound']
  PrivacyPensionResult = int(InvestmentPay)*int(PensionRateReturn)
  return render(request, '', {'InvestmenPay':InvestmentPay, 'PensionRateReturn': PensionRateReturn,'MonthCompound':MonthCompound,'PrivacyPensionResult':PrivacyPensionResult})

