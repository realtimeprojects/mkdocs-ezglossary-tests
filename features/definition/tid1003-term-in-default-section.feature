@release
@definition
@tid:1003
Feature: A term definition with default section is identified
    In order to be able to link terms to their definition
    term definitions without sections specification should be recognized and correctly
    anchored.

    Scenario: Term definition with section
	Given I set the configuration "use_default" to "true"
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
	Then I see the term definition "defaultterm1" in section "_"
	Then the term definition "defaultterm1" has description "Definition of defaultterm1"
	Then the term definition "defaultterm2" has description "Definition of defaultterm2"
