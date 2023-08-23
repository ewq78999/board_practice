from django.urls import path
from . import views

app_name = 'posts_practice'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    
    path('<int:id>', views.delete, name='delete'),
    
    path('<int:id>', views.edit, name='edit'),
    path('<int:id>', views.update, name='update'),
    
]
