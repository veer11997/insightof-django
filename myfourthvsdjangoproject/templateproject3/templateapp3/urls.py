from.import views
from django.urls import path

urlpatterns = [
    path('dateView/', views.dateView,name='index'),
   path('timeView/', views.timeView,name='index'), 
    
]
