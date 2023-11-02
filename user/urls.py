from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("picture/", views.upload_picture_user, name="picture"),
    path("profile/<int:pk>", views.profile, name="profile"),
]
