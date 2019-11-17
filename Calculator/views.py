from django.shortcuts import render



def management(request):
    return render(request,'management.html')

def management2(request):
    return render(request,'management2.html')


def management3(request):
    return render(request,'management3.html')

# Create your views here.
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
