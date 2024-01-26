import string
import random
from playwright.sync_api import Page
import config
import qase


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "//*[@aria-label='Поиск в Google']"
    _REPORT_PATH = "report/screenshot/"

    def click_on_button_by_name(self, page: Page, button_name) -> None:
        _SELECTORS = [
            f"//*[contains (@class, 'button') and text() = '{button_name}']",
            f"//*[contains (@class, 'button') and text()[contains (., '{button_name}')]]"
        ]
        founded_button = None
        for selector in _SELECTORS:
            founded_button = page.locator(selector)
            if founded_button.count() != 0: break

        assert (founded_button and founded_button.count() != 0), 'Google Search button is not correct'
        founded_button.click()
        # qase.step(
        #     action=f'Click on {button_name}',
        #     data=config.url.DOMAIN,
        #     expected_result='The page opened'
        # )

    @qase.step(
        action='Open the Index Page',
        data=config.url.DOMAIN,
        expected_result='The page opened'
    )
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    @qase.step(
        action='Check name search button',
        expected_result='Google Search button is equal Поиск в Google'
    )
    def get_text_from_google_search_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_GOOGLE_SEARCH).first.get_attribute("value")
