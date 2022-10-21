from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('search/', views.search,name='search'),
    path('', views.home,name="home"),
    path('detail/<str:slug>/', views.PostDetail,name="postdetails"),
    


]
