from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html("<img src='{}' width='40px' style='border-radius: 50px;'>".format(object.car_photo.url))

    thumbnail.short_description = "photo"

    list_display = ('id', 'car_title', 'thumbnail', 'city', 'color', 'model',
                    'year', 'body_style', 'fuel_type', 'is_featured')

    list_display_links = ('id', 'car_title', 'thumbnail')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'model',
                     'city', 'fuel_type', 'body_style')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')


admin.site.register(Car, CarAdmin)
