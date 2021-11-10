from django.urls import path

from sber_games import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('registration', views.registration, name='registration'),
    path('user_info', views.user_info, name='user_info')
]