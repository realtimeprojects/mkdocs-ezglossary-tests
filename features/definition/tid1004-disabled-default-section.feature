@release
@definition
@tid:1004
Feature: Ignore terms in default section if default section is disabled
	The plugin ignores term definitions in the default section,
	when the `use_default` configuration is set to `false`.

    Scenario: Term definition with section
	Given I set the configuration "use_default" to "false"
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
        Then I see no term definition "defaultterm1" in section "_"
        Then I see no term definition "defaultterm2" in section "_"

    Scenario: Term definition with section still visible
	Given I set the configuration "use_default" to "false"
        When I load the "module1/definitions" page.
        Then the page title contains "Definitions"
        Then I see the term definition "term1" in section "section1"
	Then I see the term definition "term2" in section "section2"
