@release
@linking
@tid:1008
Feature: Link to a term definition
	The user is able to place a link to a term definition using the
	syntax `<section:term` anywhere in his documentation.

    Scenario: Link
        When I load the "module2/links1" page.
        Then the page title contains "Links"
	Then I see a link to "term1" in section "section1"
	Then I see a link to "term1" in section "section2"
	Then I see a link to "term2" in section "section1"
	Then I see a link to "term2" in section "section2"

	When I click the link for "term1" in section "section1"
	Then the page title contains "Definitions"

        When I load the "module2/links1" page.
	When I click the link for "term2" in section "section1"
	Then the page title contains "Definitions"

        When I load the "module2/links1" page.
	When I click the link for "term1" in section "section2"
	Then the page title contains "Definitions"

        When I load the "module2/links1" page.
	When I click the link for "term2" in section "section2"
	Then the page title contains "Definitions"
