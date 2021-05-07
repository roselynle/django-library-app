from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('books/', views.books, name='library-books'),
    path('books/new/', views.create, name='books-create'),
    path('books/<int:book_id>', views.show, name='library-show'),
]