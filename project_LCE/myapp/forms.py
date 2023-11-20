# 다양한 사용자 입력에 대한 양식
from django import forms
from .models import BankTransaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = BankTransaction
        fields = ['from_account', 'to_account', 'amount']