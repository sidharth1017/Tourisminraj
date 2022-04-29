from django.contrib import admin
from .models import *

# Register your models here.

class Touristadmin(admin.ModelAdmin):
    list_display = ('name','dname')
admin.site.register(TouristSpot, Touristadmin)

admin.site.register(TravelAgencie)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Hotel)