"""
Functional tests to check the interface during a basic game.
"""
from .base_functional_test import BaseFunctionalTest


class TestSimpleInterfaceGame(BaseFunctionalTest):

    def test_can_play_a_game_through_the_interface_with_mocked_core_game_code(self):
        # Kara and Iris decide to play a game of Colonies.
        # And so they visit the webapp.
        self.browser.get(self.live_server_url)
        assert 'Colonies' in self.browser.title

        # They are greeted with a button to start a new game and they click it.
        new_game_button = self.browser.find_element_by_id('new_game_button')
        new_game_button.click()

        # They are redirected to a game page and see a game board displayed.
        assert 'Game' in self.browser.title
        board_table = self.browser.find_element_by_id('board_table')
        for row in board_table.find_elements_by_tag_name('tr'):
            for cell in row.find_elements_by_tag_name('td'):
                assert any(character in cell for character in ['1', '2', '.'])
        self.fail('Finish the test!')

        # Kara, having never played, moves her only piece to the center of the board.

        # Iris, wanting to teach through example, promptly captures Kara's piece.

        # A display showing ending points comes up.

        # Now that Kara knows a bit more, she's determined to try again... but later. For now, they exit.
