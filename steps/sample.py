import re

from radish import then, when, world

from acre.lib import log


@when('I say {text:QuotedString}')
def i_search_for(step, text):
    log.trace("Hello World")
