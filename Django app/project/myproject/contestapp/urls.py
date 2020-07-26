from django.urls import path
from . import views

urlpatterns = [
    path('homepageview/',views.homepageview,name='index'),
    path('showdateview/',views.showdateview,name='hello'),
    path('addcontestview/', views.addcontestview,name='add'),
    path('getcontestview/',views.getcontestview,name='show')

    
]