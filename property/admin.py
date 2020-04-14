from django.contrib import admin
from .models import Flat, Complaint, Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address',)
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'created_at',
    )
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ('liked_by',)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'owners_phonenumber',
        'normalized_owners_phonenumber',
    )
    search_fields = ['owner']
    raw_id_fields = ('own_flats',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)