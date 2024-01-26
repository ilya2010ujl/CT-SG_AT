import allure
from playwright.sync_api import Page
import config
import qase


class Navigation_Action:
    @qase.step(
        action='Open the Index Page',
        data=config.url.DOMAIN,
        expected_result='The page opened'
    )
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)
        with allure.step(f"Open {config.url.DOMAIN}"):
            allure.attach(page.screenshot(), attachment_type=allure.attachment_type.PNG)
