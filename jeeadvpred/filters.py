import django_filters
from django_filters import CharFilter,ChoiceFilter
from jeeadvpred.models import rank
class RankFilter(django_filters.FilterSet):
    
    rankfield__lte = django_filters.NumberFilter(field_name='opening_rank', lookup_expr='lte')
    rankfield__gte = django_filters.NumberFilter(field_name='closing_rank', lookup_expr='gte')

    class Meta:
        model=rank
        fields = ['category','seat_pool',]
    