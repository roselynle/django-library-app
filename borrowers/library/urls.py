from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('books/<int:book_id>', views.show, name='library-show'),
]