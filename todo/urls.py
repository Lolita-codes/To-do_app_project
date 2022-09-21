from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-item', views.add_item, name='add_item'),
    path('complete/<todo_id>', views.completed_item, name='completed'),
    path('delete-completed', views.delete_completed, name='delete_completed'),
    path('delete-all', views.delete_all, name='delete_all')
]