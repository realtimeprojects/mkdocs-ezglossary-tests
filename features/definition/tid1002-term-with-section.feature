@release
@definition
@tid:1002
Feature: A term definition with specified section is identified
    In order to be able to link terms to their definition
    term definitions with sections should be recognized and correctly
    anchored.

    Scenario: Term definition with section
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
        Then I see the term definition "term1" in section "section1"
	Then the term definition "section1:term1" has description "Definition of term1"
	Then the term definition "section1:term2" has description "Definition of term2"
	Then the term definition "section2:term1" has description "Definition of term1 in section2"
	Then the term definition "section2:term2" has description "Definition of term2 in section2"
