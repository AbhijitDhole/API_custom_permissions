from django.contrib import admin
from .models import Cars
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'm_no']
admin.site.register(Cars, CarAdmin)