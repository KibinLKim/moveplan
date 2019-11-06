from django.db import models

# Create your models here.

class RetireCalculate(models.Model):
    # #퇴직연금 계산기
    # ThreeMonthCost = 평균 3개월 임금금액
    # YearPerformance = 연간 상여금 총액
    # YearAllowance = 연차수당
    ThreeMonthCost = models.CharField(max_length=100)
    YearPerformance = models.CharField(max_length=100)
    YearAllowance = models.CharField(max_length=100)
    WorkDays = models.CharField(max_length=100)
    ShowPensionDB = ((int(ThreeMonthCost) + int(YearPerformance)*3/12 + YearAllowance*3/12)/90)*30*int(WorkDays/365)   


class PrivacyPension(models.Model):
    PensionCategory =(
        ('P1','연금보험'),
        ('P2','변액연금보험'),
        ('P3','연금저축보험'),
    )
    
    PensionRateReturn = models.CharField(max_length=100)
    MonthCompound = models.CharField(max_length = 100)


class ShowPensionDC(models.Model):
    investment = (
        ('i1','10'),
        ('i2','15'),
        ('i3','20'),
    )
    YearDC = (
        ('y1','10'),
        ('y2','15'),
        ('y3','20'),
    )
    RateReturnDC = models.CharField(max_length = 100)
    TotalAllowanceDC = int(investment)*int(RateReturnDC)
    
    #get_필드명_display()
class ChoicePension(models.Model):
    WantYear = models.CharField(max_length = 100)
    ChoicePensionAnswer()