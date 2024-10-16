from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.monthly_income} on {self.date_added}"

    
class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Entertainment', 'Entertainment'),
        ('Bills', 'Bills'),
        ('Travel', 'Travel'),
        ('Other', 'Other'),
    ]
    date = models.DateField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.amount}"
