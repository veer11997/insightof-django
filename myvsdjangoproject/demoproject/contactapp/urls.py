from django.urls import path 
from.import views

urlpatterns=[
    path('',views.ContactPageView,name='index'),
    path('contact/',views.ContactPageView,name='index'),
    
]