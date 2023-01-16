from django import path
from . import views

urlpattern = [
    path('login/', views.signinPage, name="login"),
    path('logout/', views.signoutPage, name="logout"),
    path('register/', views.signupPage, name='register'),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('created-room/', views.createdRoom, name="created-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),
    path('topic/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity")
]
