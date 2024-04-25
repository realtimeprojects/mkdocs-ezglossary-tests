from radish import when

from acre.lib import log, settings
from acre.playwright import Browser


@when('I load the {page:QuotedString} page')
def i_load_page(step, page):
    log.trace(f"Loading page `{page}`")
    Browser.open(f"http://{settings.mkdocs.address}/{page}/")
