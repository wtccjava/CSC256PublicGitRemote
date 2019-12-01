Feature: Full Retirement Age Calculator
  A tool to find out when a person can retire based on the person's birth date

	Scenario Outline: Entering years, months, age, and years that test the inside of the boundaries
		Given the birth year entered is "<birthYear>"
		When the birth month entered is "<birthMonth>"
        And the retirement age is "<retireAge>"
        And the retirement month is "<retireMonth>"
		Then the retirement date is "<resultYear>" years and "<resultMonth>" months

		Examples: Boundaries
		| birthYear | birthMonth | retireAge | retireMonth |resultYear| resultMonth|
		| 1900      | 1          | 65        |  0          |  1965    |      1     |
		| 2019      | 12         | 67        | 11          |  2087	  |     10     |

		
	Scenario: Testing inside the lower boundary of birth years
		Given the value entered is a number
		When the year entered is "1900"
		Then the retirement age is "65, 0"

    Scenario: Testing outside the lower boundary of birth years
      Given the value entered is a number
      When the year entered is "1899"
      Then the result is a "ValueError"

    Scenario: Testing inside the upper boundary of birth years
		Given the value entered is a number
		When the year entered is "2019"
		Then the retirement age is "67, 0"

    Scenario: Testing outside the upper boundary of birth years
		Given the value entered is a number
		When the year entered is "2020"
		Then the result is a "ValueError"
