from django.urls import path 
from.import views

urlpatterns=[
    path('',views.homePageView,name='index'),
    path('sharma/',views.homePageView,name='index'),
    
]