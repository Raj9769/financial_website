from django.shortcuts import render, redirect, get_object_or_404
from .models import Income, Transaction
from .forms import IncomeForm, TransactionForm
from django.db.models import Sum

def home(request):
    incomes = Income.objects.all()
    return render(request, 'tracker/home.html', {'incomes': incomes})

# Display all incomes and handle Create/Update operations
def add_income(request):
    incomes = Income.objects.all()
    form = IncomeForm()

    if request.method == 'POST':
        income_id = request.POST.get('income_id', None)

        if income_id:  # Update existing income
            income = get_object_or_404(Income, id=income_id)
            form = IncomeForm(request.POST, instance=income)
        else:  # Create new income
            form = IncomeForm(request.POST)

        if form.is_valid():
            form.save()  # Save income to DB
            return redirect('add_income')

    return render(request, 'tracker/add_income.html', {'incomes': incomes, 'form': form})

# Handle income deletion
def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id)
    income.delete()
    return redirect('add_income')


def add_transactions(request):
    transactions = Transaction.objects.order_by('-date')[:5]  # Get recent transactions
    
    total_income = Income.objects.all().first()

    #Retreive real data from Database
    if total_income:
        total_income = total_income.monthly_income
    else:
        total_income = 0 
    total_expense = Transaction.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    budget_used_percentage = (total_expense / total_income) * 100 if total_income > 0 else 0

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_transactions')
    else:
        form = TransactionForm()

    return render(request, 'tracker/add_transactions.html', {
        'form': form,
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'budget_used_percentage': budget_used_percentage,
    })
