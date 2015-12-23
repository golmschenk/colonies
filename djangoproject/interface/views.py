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
    def post(self, request, *args, **kwargs):
        """
        Executes move on the game for a given move request. Continues to redirect after.

        :param request: The post request data. Should contain the move data in the POST dictionary.
        :type request: HttpRequest
        :param args: Passed args.
        :type args: list
        :param kwargs: Passed kwargs. Should contain the game primary key.
        :type kwargs: dict
        :return: The HTTP response
        :rtype: HttpResponse
        """
        game = get_object_or_404(Game, pk=kwargs['game_pk'])
        game.move(current_x=request.POST['current_x'], current_y=request.POST['current_y'],
                  new_x=request.POST['new_x'], new_y=request.POST['new_y'])
        game.save()
        return super().post(request, *args, **kwargs)

    def get_redirect_url(self, game_pk):
        """
        Redirects to the game view after the move.

        :param game_pk: The pk of the game to retrieve.
        :type game_pk: int
        :return: The game view url.
        :rtype: str
        """
        return reverse('game', kwargs={'game_pk': game_pk})
