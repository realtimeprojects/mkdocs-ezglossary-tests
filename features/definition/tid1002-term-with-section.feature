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
