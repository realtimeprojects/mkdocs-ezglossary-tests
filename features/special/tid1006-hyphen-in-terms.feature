@release
@tid:1006
Feature: Hyphens in terms are supported
	The plugin supports term definition which use
	hyphens

    Scenario: Hyphen in terms
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
        Then I see the term definition "term--abc def" in section "section4"
	Then the term definition "section4:term--abc def" has description "Definition of term--abc def"
        Then I see the term definition "--abc def" in section "section4"
	Then the term definition "section4:--abc def" has description "Definition of --abc def"
        Then I see the term definition "abc def--" in section "section4"
	Then the term definition "section4:abc def--" has description "Definition of abc def--"
