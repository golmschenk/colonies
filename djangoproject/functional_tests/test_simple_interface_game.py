"""
Functional tests to check the interface during a basic game.
"""
from unittest.mock import patch, Mock
from unittest import skip

from .base_functional_test import BaseFunctionalTest


class TestSimpleInterfaceGame(BaseFunctionalTest):

    @patch('interface.models.pickle')
    @patch('interface.models.CoreGame')
    def test_can_play_a_game_through_the_interface_with_mocked_core_game_code(self, mock_core_game_class, mock_pickle):
        # - Setup core game mock object.
        mock_core_game = Mock()
        mock_core_game.board = '1....\n.....\n.....\n.....\n....2'
        mock_core_game_class.return_value = mock_core_game
        mock_pickle.dumps.return_value = b'placeholder'
        mock_pickle.loads.return_value = mock_core_game

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
        board_table.find_element_by_tag_name('tr').find_element_by_tag_name('td')  # - At least one board tile exists.
        for row in board_table.find_elements_by_tag_name('tr'):
            for cell in row.find_elements_by_tag_name('td'):
                assert any(character in cell.text for character in ['1', '2', '.'])  # - All elements make sense.

        # Kara, having never played, moves her only piece to the center of the board.
        def move_side_effect(*args, **kwargs):
            mock_core_game.board = '.....\n.....\n..1..\n.....\n....2'
        mock_core_game.make_move.side_effect = move_side_effect
        current_x_position = self.browser.find_element_by_id('current_x_position')
        current_x_position.send_keys('0')
        current_y_position = self.browser.find_element_by_id('current_y_position')
        current_y_position.send_keys('0')
        new_x_position = self.browser.find_element_by_id('new_x_position')
        new_x_position.send_keys('2')
        new_y_position = self.browser.find_element_by_id('new_y_position')
        new_y_position.send_keys('2')
        move_button = self.browser.find_element_by_id('move_button')
        move_button.click()

        # They see Kara's piece in the middle of the board.
        board_table = self.browser.find_element_by_id('board_table')
        rows = board_table.find_elements_by_tag_name('tr')
        assert '.' == rows[0].find_elements_by_tag_name('td')[0].text
        assert '1' == rows[2].find_elements_by_tag_name('td')[2].text

        # Iris, wanting to teach through example, promptly captures Kara's piece.
        def move_side_effect(*args, **kwargs):
            mock_core_game.board = '.....\n.....\n..2..\n...2.\n....2'
            mock_core_game.status = 'Player 2 wins! Player 1: 0 | Player 2: 2'
        mock_core_game.make_move.side_effect = move_side_effect
        current_x_position = self.browser.find_element_by_id('current_x_position')
        current_x_position.send_keys('4')
        current_y_position = self.browser.find_element_by_id('current_y_position')
        current_y_position.send_keys('4')
        new_x_position = self.browser.find_element_by_id('new_x_position')
        new_x_position.send_keys('3')
        new_y_position = self.browser.find_element_by_id('new_y_position')
        new_y_position.send_keys('3')
        move_button = self.browser.find_element_by_id('move_button')
        move_button.click()

        # Kara sees that her piece has been converted to Iris' team.
        board_table = self.browser.find_element_by_id('board_table')
        rows = board_table.find_elements_by_tag_name('tr')
        assert '2' == rows[4].find_elements_by_tag_name('td')[4].text
        assert '2' == rows[3].find_elements_by_tag_name('td')[3].text
        assert '2' == rows[2].find_elements_by_tag_name('td')[2].text

        # A display showing ending points comes up.
        status = self.browser.find_element_by_id('game_status')
        assert 'Player 2 wins! Player 1: 0 | Player 2: 2' in status.text

        # Now that Kara knows a bit more, she's determined to try again... but later. For now, they exit.
        self.browser.close()

    def test_can_play_a_game_through_the_interface(self):
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
        board_table.find_element_by_tag_name('tr').find_element_by_tag_name('td')  # - At least one board tile exists.
        for row in board_table.find_elements_by_tag_name('tr'):
            for cell in row.find_elements_by_tag_name('td'):
                assert any(character in cell.text for character in ['0', '1', '.'])  # - All elements make sense.

        # Kara, having never played, moves her only piece to the center of the board.
        current_x_position = self.browser.find_element_by_id('current_x_position')
        current_x_position.send_keys('0')
        current_y_position = self.browser.find_element_by_id('current_y_position')
        current_y_position.send_keys('0')
        new_x_position = self.browser.find_element_by_id('new_x_position')
        new_x_position.send_keys('2')
        new_y_position = self.browser.find_element_by_id('new_y_position')
        new_y_position.send_keys('2')
        move_button = self.browser.find_element_by_id('move_button')
        move_button.click()

        # They see Kara's piece in the middle of the board.
        board_table = self.browser.find_element_by_id('board_table')
        rows = board_table.find_elements_by_tag_name('tr')
        assert '.' == rows[0].find_elements_by_tag_name('td')[0].text
        assert '0' == rows[2].find_elements_by_tag_name('td')[2].text

        # Iris, wanting to teach through example, promptly captures Kara's piece.
        current_x_position = self.browser.find_element_by_id('current_x_position')
        current_x_position.send_keys('4')
        current_y_position = self.browser.find_element_by_id('current_y_position')
        current_y_position.send_keys('4')
        new_x_position = self.browser.find_element_by_id('new_x_position')
        new_x_position.send_keys('3')
        new_y_position = self.browser.find_element_by_id('new_y_position')
        new_y_position.send_keys('3')
        move_button = self.browser.find_element_by_id('move_button')
        move_button.click()

        # Kara sees that her piece has been converted to Iris' team.
        board_table = self.browser.find_element_by_id('board_table')
        rows = board_table.find_elements_by_tag_name('tr')
        assert '1' == rows[4].find_elements_by_tag_name('td')[4].text
        assert '1' == rows[3].find_elements_by_tag_name('td')[3].text
        assert '1' == rows[2].find_elements_by_tag_name('td')[2].text

        # A display showing ending points comes up.
        # status = self.browser.find_element_by_id('game_status')
        # assert 'Player 2 wins! Player 1: 0 | Player 2: 2' in status.text

        # Now that Kara knows a bit more, she's determined to try again... but later. For now, they exit.
        self.browser.close()