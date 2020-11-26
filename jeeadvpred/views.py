from django.shortcuts import render
from jeeadvpred.filters import RankFilter
from jeeadvpred.models import rank

def rank_predictor(request):
    rank_list = rank.objects.order_by('institute_name')
    rank_filter = RankFilter(request.GET, queryset=rank_list)
    return render(request, 'jeeadvpred/rank.html', {'filter': rank_filter})

    
    
    
            
   
    