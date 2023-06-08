from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('creteRoom', views.createRoom, name='createRoom'),
    path('updateRoom/<str:pk>/', views.updateRoom, name='updateRoom'),
    path('deleteRoom/<str:pk>/', views.deleteRoom, name='deleteRoom'),
    path('login/', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('update-user/', views.updateUser, name='update-user'),
     path('topics/', views.topicPage, name='topics'),
     path('activity/', views.activityPage, name='activity'),
    
    
]
