import allure
from playwright.sync_api import Page

import config
import qase


class Button_Action:

    def click_on_button_by_name(self, page: Page, button_name) -> None:
        _SELECTORS = [
            f"//*[contains (@class, 'button') and text() = '{button_name}']",
            f"//*[contains (@class, 'button') and text()[contains (., '{button_name}')]]",
            f"//button[text()[contains (., '{button_name}')]]"
        ]

        founded_button = None
        for selector in _SELECTORS:
            founded_button = page.locator(selector)
            if founded_button.count() != 0: break

        assert (founded_button and founded_button.count() != 0), f"Can't find button with name {button_name}"
        founded_button.first.click()
        with allure.step(f"Click on {button_name} button"):
            allure.attach(page.screenshot(), attachment_type=allure.attachment_type.PNG)
        # qase.step(
        #     action=f'Click on {button_name}',
        #     data=config.url.DOMAIN,
        #     expected_result='The page opened'
        # )
