"""
The URL routing for the interface app.
"""
from django.conf.urls import url

from interface.views import GameView, NewGameView

urlpatterns = [
    url(r'^/game/new$', NewGameView.as_view(), name='new-game'),
    url(r'^/game/(?P<game_id>\d+)$', GameView.as_view(), name='game'),
    url(r'^/game$', GameView.as_view(), name='game'),
]
