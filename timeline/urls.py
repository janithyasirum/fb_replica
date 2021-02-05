from django.urls import path

from . import views

app_name = 'timeline'

urlpatterns = [
    path('wall_post', views.wall_post_view, name='wall_post'),
    path('comment_post/<int:post_id>/', views.comment_post_view, name='comment_post'),
    path('like_post/<int:post_id>/', views.like_post_view, name='like_post'),
    path('unlike_post/<int:post_id>/', views.unlike_post_view, name='unlike_post'),
    path('like_comment/<int:comment_id>/', views.like_comment_view, name='like_comment'),
    path('unlike_comment/<int:comment_id>/', views.unlike_comment_view, name='unlike_comment'),
]
