from django.shortcuts import render, redirect, get_object_or_404
from hello.models import RetireCalculate, PrivacyPension



def management(request):
  return render(request, 'management.html')

def management_send(request):
  if request.method == 'POST':
      retire = RetireCalculate()
      retire.YearPerformance = request.POST.get['YearPerformance','']
      retire.ThreeMonthCost = request.POST.get['ThreeMonthCost','']
      retire.YearAllowance = request.POST.get['YearAllowance','']
      retire.WorkDays = request.POST.get['WorkDays','']
      Revenue = (int(retire.ThreeMonthCost)+int(retire.YearPerformance)*3/12 + int(retire.YearAllowance)*3/12)
      Revenue2 = Revenue/90*30*(int(retire.WorkDays)/365)
      retire.RetireExpected = Revenue2
      retire.save()
      return redirect('management2')

def management2(request):
    return render(request,'management2.html')

def management3(request):
    return render(request,'management3.html')

def management3_send(request):
    privacy = PrivacyPension()
    privacy.PensionCategory = request.GET('PensionCategory')
    privacy.PensionRateReturn = request.GET('PensionRateReturn')
    privacy.MonthCompound = request.GET('MonthCompound')
    privacy.save()
    return redirect(request, 'information1')

# Create your views here.


def information1(request):
  ExpectedRevenue = RetireCalculate.objects
  return render(request, 'information1.html', {'ExpectedRevenue':ExpectedRevenue})
  

def PrivacyPension(request):
  InvestmentPay = request.GET['InvestmentPay']
  PensionRateReturn = request.GET['PensionRateReturn']
  MonthCompound = request.GET['MonthCompound']
  PrivacyPensionResult = int(InvestmentPay)*int(PensionRateReturn)
  return render(request, '', {'InvestmenPay':InvestmentPay, 'PensionRateReturn': PensionRateReturn,'MonthCompound':MonthCompound,'PrivacyPensionResult':PrivacyPensionResult})


def ChoicePension(request):
  WantYear = request.GET['WantYear']
  RetireExpected = request.GET['RetireExpected']
  MonthPayment = int(WantYear)*int(RetireExpected)*0.017/int(WantYear)/12
  return render(request, '',{'WantYear':WantYear, 'RetureExpected':RetireExpected, 'MonthPayment':MonthPayment})

def RetireSeason(request):
  OneYearChoice = request.GET['OneYearChoice']
  AddMonth = request.GET['AddMonth']
  RestDate = request.GET['RestDate']
  Workdays = request.GET['Workdays']
  ThreeMonthCost = request.GET['ThreeMonthCost']
  YearPerformance = request.GET['YearPerformance']
  YearAllowance = request.GET['YearAllowance']
  if OneYearChoice == '네':
    a = int(ThreeMonthCost)*1.1 + int(YearPerformance)*3/12+ int(YearAllowance)*3/12
    b = a/90*int(Workdays)/365
  return render(request,'',{'AllPayment':b})



# def NationalPension(request):
#     Birthday1 = request.GET['Birthday1']
#     FirstDate = request.GET['FirstDate']
#     LastDate = int(Birthday1)+60
#     ExpectedRaise = request.GET['ExpectedRaise']
#     StartofMoney = FirstDate
#     EndofMoney = '2019년 11월'
#     MoneyDate = 2019
#     MoneyRate = request.GET['MoneyRate']
#     p1 = 
#     p2 =
#     p3 =
#     p4 =
#     if p >= 32*12:
#     AllDate2 = request.GET['AllDate2']
#     NationalPensionResult = [2019-(AllDate/12)
#     return 
