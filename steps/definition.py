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
        return world.page.locator(str(self._xpath))

    @property
    def _xpath(self):
        id = glossary.get_id(self._section, self._term, "defs", 0)
        return xpath.article.dt().has(xpath.a(id=id, text=f"*{self._term}"))

    @property
    def description(self):
        return world.page.locator(str(xpath.dd.following(self._xpath))).first


@then('I see the term definition {term:QuotedString} in section {section:QuotedString}')
def i_see_term(step, section, term):
    log.trace(f"Checking definition for {section}:{term}")
    assert Definition(section, term).exists(), f"{section}:{term} definition not found"


@then('the term definition {term:QuotedString} has description {description:QuotedString}')
def term_has_description(step, term, description):
    if ":" in term:
        (section, term) = term.split(":")
    else:
        (section, term) = ("_", term)

    log.trace(f"Checking definition for {section}:{term}")
    defn = Definition(section, term)
    log.debug(f"--- {defn.description.text_content()}")
    defn.description.filter(has_text=description)
