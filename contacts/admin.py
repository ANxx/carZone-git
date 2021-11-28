from django.contrib import admin

from contacts.models import Contact

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('id', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname', 'email', 'car_title')
    list_per_page = 25

admin.site.register(Contact,contactAdmin)