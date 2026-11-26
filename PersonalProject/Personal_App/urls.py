from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('mainPage/', views.main_page, name = 'mainpage'),
    path('createNote/', views.createNote_view, name = 'createNote'),
    path('update/<int:note_id>/', views.updateNote, name = 'updateNote'),
    path('delete/<int:note_id>/', views.deleteNote, name = 'deleteNote'),
    path('logout/', views.logout_view, name = 'logout'),
]