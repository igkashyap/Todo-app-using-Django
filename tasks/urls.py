from django.urls import path
from .views import index, updatetask, deletetask

urlpatterns =[
    path('',index, name='index'),
    path('update/<str:pk>/', updatetask, name='update'),
    path('delete/<str:pk>/', deletetask, name='delete'),
]