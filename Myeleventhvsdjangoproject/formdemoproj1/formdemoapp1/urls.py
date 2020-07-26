from django.urls import path
from.import views
urlpatterns=[
    path('addbooks/',views.addBooksView,name='books'),
    path('search_books/',views.searchFormView,name='Searchform'),
    path('search/',views.searchView,name='search'),
]