# 다양한 사용자 입력에 대한 양식
from django import forms
from .models_banking import BankTransaction


# 202405110138 김용록 
class Transaction_HospitalForm(forms.ModelForm):
    class Meta:
        model = BankTransaction
        