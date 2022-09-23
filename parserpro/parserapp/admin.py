from django.contrib import admin
from parserapp.models import UserRegistration


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname','state','district','rdate']
    ordering = ['rdate']


admin.site.register(UserRegistration, UserAdmin)