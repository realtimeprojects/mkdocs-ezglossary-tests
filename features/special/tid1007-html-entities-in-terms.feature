@release
@tid:1007
Feature: HTML entities in terms
	Since the usage of certain characters in terms is restricted,
	the user is able to use html entities as their replacement in term definitions.

    Scenario: Unicode in terms
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
        Then I see the term definition "abc&def" in section "section4"
	Then the term definition "section4:abc&def" has description "Definition of abc&def"
