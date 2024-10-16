from django import forms
from .models import Income, Transaction

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['monthly_income']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'description', 'category', 'amount']
