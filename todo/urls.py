from django.urls import path

# meng-import my_view dari App todo
from .views import index_view, detail_view, create_view, update_view, delete_view

# nama app
app_name = 'todo'   
urlpatterns = [
    # route untuk page index
    path('', index_view, name='index'),
    
    # route untuk page detail
    path('<int:task_id>', detail_view, name='detail'),
    
    # route untuk page tambah task
    path('create', create_view, name='create'),
    
    # route untuk page ubah task
    path('update/<int:task_id>', update_view, name='update'),
    
    # route untuk delete task
    path('delete/<int:task_id>', delete_view, name='delete'),
]