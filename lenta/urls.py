from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_lenta),
    path('posts/<int:pk>/', views.detail_post),
    path('edit-post/<int:pk>/', views.edit_post),
    path('like-add', views.add_like),
    path('comment-add', views.add_comment),
    path('post-add/', views.add_post),
]
