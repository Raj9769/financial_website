from django.contrib import admin
from .models import Income, Transaction

# Register your models here.
admin.site.register(Income),
admin.site.register(Transaction)