# TODO: Implement Routings Here
from django.urls import path
from . import views
app_name = 'todolist'

urlpatterns = [
    path('', views.show_todolist, name='show_todolist'),
    path('add/', views.add_todolist, name='add_todolist'),
    path('json/', views.show_json, name='show_json'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register, name='register'),
    path('create-task/', views.create_task, name='create_task'),




]
