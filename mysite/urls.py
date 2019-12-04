from django.urls import path
from mysite.views import index, index_detail

urlpatterns = [
    path('', index, name='index'),
    path('hello/<int:pk>/', index_detail, name='index_detail'),
]

