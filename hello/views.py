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

def management(request):
    return render(request,'management.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

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
