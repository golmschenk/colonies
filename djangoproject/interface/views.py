"""
The interface's view functions.
"""
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from interface.models import Game


class HomeView(TemplateView):
    """
    The home view class. For displaying the basic landing page.
    """
    template_name = 'home.html'


class NewGameView(RedirectView):
    """
    The redirect view to create a new game.
    """
    def get_redirect_url(self):
        """
        Creates the new game an redirects to the game view with the new game's ID passed.

        :return: The redirect url of the new game.
        :rtype: str
        """
        game = Game.objects.create()
        return reverse('game', kwargs={'game_id': game.id})


class GameView(TemplateView):
    """
    The game view class. For displaying the game interface page.
    """
    template_name = 'game.html'

    def get_context_data(self, game_id):
        """
        Prepares the game data to pass as the context to the template.

        :param game_id: The game to retrieve.
        :type game_id: Game
        :return: The context of the template.
        :rtype: dict
        """
        game = get_object_or_404(Game, pk=game_id)
        return {'board_rows': game.board_rows}
