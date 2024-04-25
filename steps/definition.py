from radish import then, world
from yaxp import xpath

from acre.lib import log

from mkdocs_ezglossary_plugin import glossary


class Definition:
    def __init__(self, section, term):
        self._section = section
        self._term = term

    def exists(self):
        try:
            self._locator.wait_for()
        except Exception:
            return False
        return True

    @property
    def _locator(self):
        # return world.page.get_by_role("link").filter(has_text=self._term)
        id = glossary.get_id(self._section, self._term, "defs", 0)
        return world.page.locator(str(xpath.article.dt().has(xpath.a(id=id, text=f"*{self._term}"))))

    @property
    def definition(self):
        return self._locator().get_next_sibling()


@then('I see the term definition {term:QuotedString} in section {section:QuotedString}')
def i_search_for(step, section, term):
    log.trace(f"Checking definition for {section}:{term}")
    assert Definition(section, term).exists(), f"{section}:{term} definition not found"
