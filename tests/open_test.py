import time

import pytest
import pages


class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        actual_text = pages.index_page.get_text_from_google_search_button(page)
        assert actual_text == 'Поиск в Google', 'Google Search button is not correct'