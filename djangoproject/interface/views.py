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
        game = Game.objects.create_game()
        return reverse('game', kwargs={'game_pk': game.pk})


class GameView(TemplateView):
    """
    The game view class. For displaying the game interface page.
    """
    template_name = 'game.html'

    def get_context_data(self, game_pk):
        """
        Prepares the game data to pass as the context to the template.

        :param game_pk: The pk of the game to retrieve.
        :type game_pk: int
        :return: The context of the template.
        :rtype: dict
        """
        game = get_object_or_404(Game, pk=game_pk)
        return {'board_rows': game.board_rows}


class MoveView(RedirectView):
    """
    The redirect view to make a move.
    """
    def get_redirect_url(self, game_pk, current_x, current_y, new_x, new_y):
        """
        Executes move on the game for a given move request. Redirects to the game view after.

        :param game_pk: The pk of the game to retrieve.
        :type game_pk: int
        :param current_x: Current x position of piece to move.
        :type current_x: int
        :param current_y: Current y position of piece to move.
        :type current_y: int
        :param new_x: The x position to move the piece to.
        :type new_x: int
        :param new_y: The y position to move the piece to.
        :type new_y: int
        :return: The game view url.
        :rtype: str
        """
        game = get_object_or_404(Game, pk=game_pk)
        game.move(current_x=current_x, current_y=current_y, new_x=new_x, new_y=new_y)
        return reverse('game', kwargs={'game_pk': game_pk})
