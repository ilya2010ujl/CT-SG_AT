import string
import random

import allure
from playwright.sync_api import Page
import config
import qase


class Field_Action:

    def type_text_in_field_by_name(self, page: Page, field_name, text) -> None:
        _SELECTORS = [
            f"//*[text()[contains (., '{field_name}')]]/parent::div/input"
        ]

        founded_field = None
        for selector in _SELECTORS:
            founded_field = page.locator(selector)
            if founded_field.count() != 0: break

        assert (founded_field and founded_field.count() != 0), f"Can't find field with name {field_name}"
        founded_field.first.type(text)
        with allure.step(f"Type {text} text in {field_name}"):
            allure.attach(page.screenshot(), attachment_type=allure.attachment_type.PNG)

    # qase.step(
        #     action=f'Click on {button_name}',
        #     data=config.url.DOMAIN,
        #     expected_result='The page opened'
        # )

    def tooltip_for_field_is(self, page: Page, field_name, tooltip) -> None:
        _SELECTORS = [
            f"//*[text()[contains (., '{field_name}')]]/parent::div/*[contains (@class, 'alert')]"
        ]

        founded_tooltip = None
        for selector in _SELECTORS:
            founded_tooltip = page.locator(selector)
            if founded_tooltip.count() != 0: break
        tooltip_text = founded_tooltip.first.inner_text()
        assert tooltip in tooltip_text, f"ER tooltip is ${tooltip}, AR tooltip is ${tooltip_text}"
        with allure.step(f"Check tooltip is {tooltip_text} for {field_name} field"):
            allure.attach(page.screenshot(), attachment_type=allure.attachment_type.PNG)
