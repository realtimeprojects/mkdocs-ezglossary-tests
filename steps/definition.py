from radish import then, world
from yaxp import xpath
import html

from acre.lib import log
from acre import controls

from mkdocs_ezglossary_plugin import glossary


class TermDefinition(controls.Control):
    def __init__(self, term, section=None, parent=None):
        super().__init__(parent)
        self._section = section if section else "_"
        self._term = term

    @property
    def locator(self):
        return self.parent.locator(str(self._xpath))

    @property
    def _xpath(self):
        id = glossary.get_id(self._section, self._term, "defs", 0)
        return xpath.article.dt().has(xpath.a(id=id, text=f"*{html.unescape(self._term)}"))

    @property
    def description(self):
        return world.page.locator(str(xpath.dd.following(self._xpath))).first


@then('I see the term definition {term:QuotedString} in section {section:QuotedString}')
def i_see_term(step, section, term):
    log.trace(f"Checking definition for {section}:{term}")
    TermDefinition(term, section).wait_for()


@then('I see no term definition {term:QuotedString} in section {section:QuotedString}')
def i_see_no_term(step, section, term):
    assert not TermDefinition(term, section).exists(), f"{section}:{term} definition found"


@then('the term definition {term:QuotedString} has description {description:QuotedString}')
def term_has_description(step, term, description):
    if ":" in term:
        (section, term) = term.split(":")
    else:
        (section, term) = (None, term)

    log.trace(f"Checking definition for {section}:{term}")
    defn = TermDefinition(term, section)
    log.debug(f"--- {defn.description.text_content()}")
    defn.description.filter(has_text=description).wait_for()
