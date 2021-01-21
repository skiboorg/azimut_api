from django.contrib import admin
from .models import *

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 0

class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    class Meta:
        model = Car

admin.site.register(Car,CarAdmin)
admin.site.register(Service)
admin.site.register(AutoCategory)
admin.site.register(AutoSubCategory)
admin.site.register(CarOptions)

