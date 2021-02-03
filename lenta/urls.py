from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('edit-post/<int:pk>/', views.edit_post),
    path('like-add', views.add_like),
    path('comment-add', views.add_comment),
    path('post-add/', views.PostCreateView.as_view()),
]
