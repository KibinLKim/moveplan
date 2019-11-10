from django.db import models

# Create your models here.

class RetireCalculate(models.Model):
    # #퇴직연금 계산기
    # ThreeMonthCost = 평균 3개월 임금금액
    # YearPerformance = 연간 상여금 총액
    # YearAllowance = 연차수당
    ThreeMonthCost = models.IntegerField()
    YearPerformance = models.IntegerField()
    YearAllowance = models.IntegerField()
    WorkDays = models.IntegerField()
    RetireExpected = models.CharField(max_length=255, default='example') 

    # 계산 및 데이터 베이스 저장
 


class PrivacyPension(models.Model):
    PensionCategory =(
        ('P1','연금보험'),
        ('P2','변액연금보험'),
        ('P3','연금저축보험'),
    )
    PensionCategoryChoices = models.CharField(max_length=60, choices = PensionCategory,default=0)
    InvestmentPay = models.CharField(max_length = 100)
    PensionRateReturn = models.CharField(max_length=100)
    MonthCompound = models.CharField(max_length = 100)


class ShowPensionDC(models.Model):
    Investment = (
        ('i1','10'),
        ('i2','15'),
        ('i3','20'),
    )
    YearDC = (
        ('y1','10'),
        ('y2','15'),
        ('y3','20'),
    )
    InvestmentChoices = models.CharField(max_length=60, choices = Investment, default = 0)
    YearDCChoices = models.CharField(max_length=60, choices = YearDC, default = 0)
    RateReturnDC = models.CharField(max_length = 100)
    
    #get_필드명_display()
class ChoicePension(models.Model):
    WantYear = models.CharField(max_length = 100)
