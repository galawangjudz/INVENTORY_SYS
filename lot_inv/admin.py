from django.contrib import admin
from .models import LotInv
from .models import ProjectList
# Register your models here.


admin.site.site_header ="Lot Inventory Admin"
admin.site.site_title ="Lot Inventory Area"
admin.site.index_title ="Welcome to the Lot Inventory Area"


class LotAdmin(admin.ModelAdmin):
    list_display = ['c_lid',
                    'c_site',
                    'c_block',
                    'c_lot',
                    'c_lot_area',
                    'c_price_sqm',
                    'c_remarks',
                    'c_status',
                    'c_lot_type',
                    'c_title',
                    'c_lot_type_remarks',
                    'c_title_owner',
                    'c_previous_owner']
        

    search_fields = ['c_lid',
                    'c_site',
                    'c_block',
                    'c_lot',
                    'c_lot_area',
                    'c_price_sqm',
                    'c_remarks',
                    'c_status',
                    'c_lot_type',
                    'c_title',
                    'c_lot_type_remarks',
                    'c_title_owner',
                    'c_previous_owner']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['c_acronym','c_code','c_name','c_location']

    search_fields = ['c_acronym']
        


admin.site.register(LotInv, LotAdmin)
admin.site.register(ProjectList, ProjectAdmin)



