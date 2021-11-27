from django.contrib import admin
from django.utils.html import format_html
from .models import Car

# Register your models here.
class carAdmin(admin.ModelAdmin): # Class for displaying content on admin page
    def thumbnail(self,obj):  # Thumbnail Display /admin page
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(obj.car_photo.url))
    
    thumbnail.short_description = 'Photo'

    list_display = ('id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured') # Admin Display 
    list_display_links = ('id','thumbnail','car_title')

    list_editable = ('is_featured',)

    search_fields = ('id','car_title','city','model','body_style','fuel_type') # Admin Search 

    list_filter = ('city', 'model','body_style','fuel_type') # Admin Filter


admin.site.register(Car,carAdmin)
