from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),

    path(
    'photo/<int:photo_id>/<str:action>/',
    views.photo_interaction,
    name='photo_interaction'
),
]