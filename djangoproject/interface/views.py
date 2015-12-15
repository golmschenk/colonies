"""
The interface's view functions.
"""
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse

from interface.models import Game


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


class NewGameView(RedirectView):
    """
    The redirect view to create a new game.
    """
    def get_redirect_url(self, *args, **kwargs):
        game = Game.objects.create()
        return reverse('game', kwargs={'game_id': game.id})