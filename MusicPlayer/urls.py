from django.urls import path
from . import views

urlpatterns = [
  path("login/", views.loginpage, name="Login"),
  path("register/", views.register, name="Register"),
  path('', views.home, name='Home'),
  path('search/', views.home, name='search'),
  path('about/', views.about, name='About'),
  path("logout/", views.logoutuser, name="Logout"),
  path('watchlater/', views.watch_later_list, name='watchlater'),
  path('addtowatchlater/<int:song_id>/', views.add_to_watch_later, name='addtowatchlater')
]