from django.urls import path
from .views import *



urlpatterns = [
    path("game/<int:pk>/", GamesAPIView.as_view(),name='game'),
    path("game/", CreategameAPIView.as_view(),name='game'),
    path("games/", GameslistAPIView.as_view(),name='games'),
    path('levelbyuserid/<int:id>/',LevelByUserId.as_view()),
    ]