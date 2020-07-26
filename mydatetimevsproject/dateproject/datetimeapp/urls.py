from django.urls import path
from .import views


urlpatterns = [
       path('showdate/',views.dateView,name='index'),
       path('showtime/',views.timeView,name='index')

]