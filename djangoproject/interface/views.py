"""
The interface's view functions.
"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    The home view class. For displaying the basic landing page.
    """
    template_name = 'home.html'


class GameView(TemplateView):
    """
    The game view class. For displaying the game interface page.
    """
    template_name = 'game.html'
