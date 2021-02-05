from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),

    path('logout', views.logout_view, name='logout'),
    path('members', views.members_view, name='members'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
]
