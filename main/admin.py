from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','phno','email','address')
    search_fields=('name','phno')
admin.site.register(Contact,ContactAdmin)
