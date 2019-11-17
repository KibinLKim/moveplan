from django.db import models
from django.contrib.auth.models import AbstractUser



#New User Class Name  # Name, E-mail, PW is already existed in User base Model
class MoveplanUser(AbstractUser):
    #Necessary Table
    #생년월일
    userBirthYearDay = models.CharField(max_length=6,default="",blank=False)
    # ThreeMonthCost = 평균 3개월 임금금액
    # YearPerformance = 연간 상여금 총액
    # YearAllowance = 연차수당
    # WorkDays = 근속일수
    ThreeMonthCost = models.IntegerField(default=1)
    YearPerformance = models.IntegerField(default=1)
    YearAllowance = models.IntegerField(default=1)
    WorkDays = models.IntegerField(default=1)
    RetireExpected = models.CharField(max_length=255, default='example') 


