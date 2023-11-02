from django.urls import path
from . import views

urlpatterns = [
    #paths for 
    path('', views.home, name='home'),
    path('games_interface/', views.games_interface, name='games_interface'),
    path('delete_game/<int:game_id>/', views.delete_game, name='delete_game'),
    path('report_interface/', views.report_interface, name='report_interface'),
]