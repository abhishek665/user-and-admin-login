from django.contrib import admin
from django.urls import path
from .import views

#TEMPLATES URL
app_name = 'hello'

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),

    path('user_login/', views.user_login, name='user_login'),

    path('user_logout/', views.user_logout, name='user_logout'),

    path('delete_db/', views.delete_db,name='delete_db'),

    path('delete_account/', views.delete_account, name='delete_account'),

    path('show_db/', views.show_db, name='show_db'),

    path('edit_account/<int:id>', views.edit_account, name='edit_account'),


] 