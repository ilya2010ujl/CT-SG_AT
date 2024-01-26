import string
import random


class Allure:
    def take_screenshot(self, page: Page) -> str:
        screenshot_path = self._REPORT_PATH + ''.join(random.choices(string.ascii_lowercase, k=20)) + '.png'
        page.screenshot(path=screenshot_path)
        return screenshot_path
