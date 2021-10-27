from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()


# Create your models here.

class ProjectList(models.Model):
    c_acronym = models.CharField(max_length=10, verbose_name= 'acronym')
    c_code = models.CharField(max_length= 5, verbose_name= 'code')
    c_name = models.CharField(max_length=100, verbose_name= 'name')
    c_location = models.CharField(max_length=100, verbose_name= 'location')

    def __str__(self):
        return self.c_acronym


class LotInv(models.Model):
    STATUS = (
            ('Available','Available'), 
            ('Sold','Sold'),
            ('On Hold','On Hold'),
             ('Reserved','Reserved'),
             ('Packaged','Packaged')
            )

    TITLE = (
            ('With Title','With Title'),
            ('Without Title','Without Title')
    )
    LOT_TYPE = (
            ('Regular Lot','Regular Lot'),
            ('Prime Lot','Prime Lot')
    )
    PHASE = list(ProjectList.objects.order_by('c_acronym').values_list('c_code','c_acronym'))


    #PHASE = (ProjectList.objects.filter(c_acronym))


    c_lid = models.CharField(max_length=8, verbose_name= 'lid')
    c_site = models.IntegerField(verbose_name = 'site', null=True, choices = PHASE)
    #c_site = models.IntegerField(verbose_name = 'site')
    c_block = models.IntegerField( verbose_name= 'block')
    c_lot = models.IntegerField( verbose_name= 'lot')
    c_lot_area = models.IntegerField(verbose_name= 'lot_area')
    c_price_sqm = models.IntegerField( verbose_name= 'price_sqm')
    c_remarks = models.CharField(max_length=200, verbose_name = 'remarks')
    c_status = models.CharField(max_length=50,null=True, choices = STATUS)
    c_lot_type = models.CharField(max_length=50, null=True, choices = LOT_TYPE)
    c_title = models.CharField(max_length=50, null=True, choices = TITLE)
    c_lot_type_remarks = models.CharField(max_length=200, verbose_name = 'lot_type_remarks')
    c_title_owner = models.CharField(max_length=50, verbose_name = 'title_owner')
    c_previous_owner = models.CharField(max_length=50, verbose_name = 'previous_owner')
    
    def __str__(self):
        return self.c_lid




   

