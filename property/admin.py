from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    list_editable = ['new_building']
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
