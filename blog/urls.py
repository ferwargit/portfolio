from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
]
