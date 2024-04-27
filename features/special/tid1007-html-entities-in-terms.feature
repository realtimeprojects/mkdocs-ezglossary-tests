@release
@tid:1007
Feature: HTML entities in terms
	Since the usage of certain characters in terms is restricted,
	the user is able to use html entities as their replacement in term definitions.

    Scenario: Use of &amp; in terms
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
        Then I see the term definition "abc&amp;def" in section "section4"
	Then the term definition "section4:abc&amp;def" has description "Definition of abc&def"

    Scenario: Use of &quot; in terms
        When I load the "module1/definitions2" page.
        Then the page title contains "Advanced Definitions"
        Then I see the term definition "abc&quot;def" in section "section5"

        When I load the "module3/links2" page.
	When I click the link for "abc&quot;def" in section "section5"
	Then the page title contains "Advanced Definitions"
