@release
@definition
@tid:1005
Feature: Unicode characters in terms are supported
	The plugin supports term definition which use
	the full range of unicode characters.

    Scenario: Unicode in terms
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
        Then I see the term definition "term_✅" in section "section3"
	Then the term definition "section3:term_✅" has description "Definition of term_✅"
	Then the term definition "section3:✅" has description "Definition of ✅"
	Then the term definition "section3:✅_hello" has description "Definition of hello_✅"
