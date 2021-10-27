import django_filters

from .models import LotInv



class LotInvFilters(django_filters.FilterSet):

    class Meta:
        model = LotInv
        fields = ('c_site', 'c_block', 'c_lot')