from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" STYLE="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = "Car Image"
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model')
    list_filter = ('city', 'model', 'body_style', 'car_title')
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'milage', 'is_featured')

# Register your models here.
admin.site.register(Car, CarAdmin)