from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner','town','address')
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'normalised_owners_phonenumber'
    )
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ('liked_by',)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)