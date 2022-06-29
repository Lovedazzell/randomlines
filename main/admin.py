from django.contrib import admin
from . models import Contactus
# Register your models here.
# admin.register(Contactus)
class Contact_us(admin.ModelAdmin):
    list_display =['name', 'email', 'number', 'message']

admin.site.register(Contactus,Contact_us)