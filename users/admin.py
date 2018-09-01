from django.contrib import admin
from .models import AccountHolder

# Register your models here.

class AccountHolderAdmin(admin.ModelAdmin):
	pass

admin.site.register(AccountHolder, AccountHolderAdmin)