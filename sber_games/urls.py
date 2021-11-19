from django.urls import path

from sber_games import views
from sber_games.views import TournamentFormView, TournamentListView

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('user_info', views.user_info, name='user_info'),
    path('team', views.my_team, name='my_team'),

    path('tournament/', TournamentFormView.as_view()),
    path('tournament_list/', TournamentListView.as_view()),

    #path('profiles/<int:profile_id>/edit/', TournamentFormView.as_view()),

    path('game', views.my_game, name='my_game'),
    path('user_list', views.UserListView.as_view(), name='user_list'),
    path('user_list/<int:pk>', views.UserDetailView.as_view(), name='user_Detail')
]