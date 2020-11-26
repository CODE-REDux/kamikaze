from django.urls import path
from jeeadvpred import  views
urlpatterns = [
    path('', views.rank_predictor, name='ranks'),

]