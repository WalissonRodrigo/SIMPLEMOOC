from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'name', 'is_active', 'is_staff', 'date_joined']
	search_fields = ['username', 'email', 'name', 'is_active', 'is_staff', 'date_joined']
	prepopulated_fields = {'username':('name', 'email')}


admin.site.register(User, UserAdmin)
