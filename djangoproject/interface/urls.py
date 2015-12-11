"""
The URL routing for the interface app.
"""
from django.conf.urls import url

from interface.views import HomeView, GameView

urlpatterns = [
    url(r'^game', GameView.as_view(), name='game'),
]
