from django.urls import path
from . import views
urlpatterns = [
    path('addcontestview/', views.addcontestview,name='add'),
    path('getcontestview/',views.getcontestview,name='show')
]
