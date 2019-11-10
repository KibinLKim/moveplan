from django.contrib import admin
from .models import RetireCalculate, ShowPensionDC, PrivacyPension,ChoicePension
# Register your models here.

admin.site.register(RetireCalculate)
admin.site.register(ShowPensionDC)
admin.site.register(PrivacyPension)
admin.site.register(ChoicePension)