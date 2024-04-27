from radish import when, then
import html

from acre import controls


class TermLink(controls.Link):
    def __init__(self, term, section=None, title=None):
        section = section if section else "_"
        super().__init__(text=html.unescape(term), name=f"{section}:{term}", title=title)


@then('I see a link to {term:QuotedString} in section {section:QuotedString}')
def i_see_link(step, section, term):
    TermLink(term, section).wait_for()


@when('I click the link for {term:QuotedString} in section {section:QuotedString}')
def i_click_link(step, section, term):
    TermLink(term, section).click()


@then("the link to {term:QuotedString} in section {section:QuotedString} has title {title:QuotedString}")
def link_has_title(step, section, term, title):
    TermLink(term, section, title).wait_for()
