from django.urls import path
from.import views

urlpatterns=[

    path('',views.homePage,name='book'),
  path('add/',views.homePageView,name='book'),


]