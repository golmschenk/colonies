"""
Simple checks that the layout was actually loaded.
"""

from .base_functional_test import BaseFunctionalTest


class TestLayout(BaseFunctionalTest):
    def test_smoke_for_layout(self):
        """
        A smoke test for the layout. Helps confirm the layout was actually loaded.
        """
        # Kara goes to the Colonies interface app.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices that the main title div is styled such that it's centered and
        # it doesn't span the entire window.
        title_div = self.browser.find_element_by_id('title_div')
        self.assertAlmostEqual(
            title_div.location['x'] + title_div.size['width'] / 2,
            512,
            delta=10
        )
        self.assertLess(title_div.size['width'], 950)