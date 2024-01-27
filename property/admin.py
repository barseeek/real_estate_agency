from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    list_editable = ['new_building']
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    raw_id_fields = ('liked_by', 'owners')
    inlines = [OwnerInline, ]
    exclude = ['owners']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('name', 'pure_phone')
