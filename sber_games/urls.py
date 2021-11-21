from django.urls import path

from sber_games import views
from sber_games.views import TournamentFormView, TournamentListView, TournamentDetailView, GameFormView, GameListView, \
    GameDetailView

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('user_info', views.user_info, name='user_info'),
    path('team', views.my_team, name='my_team'),

    path('tournament/', TournamentFormView.as_view()),
    path('tournament_list/', TournamentListView.as_view()),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),

    path('game/', GameFormView.as_view()),
    path('game_list/', GameListView.as_view()),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game-detail'),

    #path('game', views.my_game, name='my_game'),
    path('user_list', views.UserListView.as_view(), name='user_list'),
    path('user_list/<int:pk>', views.UserDetailView.as_view(), name='user_Detail')
]