from django.urls import path

from sber_games import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('user_info', views.user_info, name='user_info'),
    path('profile', views.user_profile, name='user_profile'),
    path('team', views.my_team, name='my_team'),
    path('tournament', views.tournament, name='tournament'),
    path('game', views.my_game, name='my_game'),
    path('user_list', views.UserListView.as_view(), name='user_list'),
    path('user_list/<int:pk>', views.UserDetailView.as_view(), name='user_Detail')
]