from playwright.sync_api import TimeoutError as pwTimeoutError

from radish import when, then, world
from yaxp import xpath


class Link:
    def __init__(self, section, term):
        self._section = section
        self._term = term

    def exists(self, timeout=1000):
        try:
            self._locator.wait_for(timeout=timeout)
        except pwTimeoutError:
            return False
        return True

    def wait_for(self):
        return self._locator.wait_for()

    def click(self):
        self._locator.click()

    @property
    def _locator(self):
        return world.page.locator(str(self._xpath))

    @property
    def _xpath(self):
        return xpath.article.a(_=f"*{self._term}", name=f"{self._section}:{self._term}")

    @property
    def description(self):
        return world.page.locator(str(xpath.dd.following(self._xpath))).first


@then('I see a link to {term:QuotedString} in section {section:QuotedString}')
def i_see_link(step, section, term):
    Link(section, term).wait_for()


@when('I click the link for {term:QuotedString} in section {section:QuotedString}')
def i_click_link(step, section, term):
    Link(section, term).click()