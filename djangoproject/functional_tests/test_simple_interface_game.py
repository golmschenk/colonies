from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class SimpleInterfaceGameTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_play_a_game_through_the_interface_with_mocked_core_game_code(self):
        # Kara and Iris decide to play a game of Colonies.
        # And so they visit the webapp.
        self.browser.get(self.live_server_url)
        assert 'Colonies' in self.browser.title

        # They are greeted with a button to start a new game and they click it.
        new_game_button = self.browser.find_element_by_id('new_game_button')

        # They now see a game board displayed.
        self.fail('Finish the test!')

        # Kara, having never played, moves her only piece to the center of the board.

        # Iris, wanting to teach through example, promptly captures Kara's piece.

        # A display showing ending points comes up.

        # Now that Kara knows a bit more, she's determined to try again... but later. For now, they exit.
