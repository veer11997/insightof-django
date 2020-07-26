from django.urls import path
from.import views
urlpatterns = [
    
    path('',views.allBooksView,name='addbook'),
    path('showbooks/',views.showBooksView,name='showbook')
]