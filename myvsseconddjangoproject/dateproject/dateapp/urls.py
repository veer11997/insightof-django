from django.urls import path
from.import views


urlpatterns=[ 
    path('',views.datePageView,name='index'),
    path('showdate/',views.datePageView,name='index'),
]