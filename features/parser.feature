Feature: Parse json

  Scenario: Parse name
    Given Some valid json
    When I parse the data
    Then the name should be "Mr Homer J Simpson"

  Scenario: Parse children
    Given Some valid json
    When I parse the data
    Then the children should be
      | Name         | Age |
      | Lisa Simpson |   7 |
      | Bart Simpson |   9 |

  Scenario: Parse address
    Given Some valid json
    When I parse the data
    Then the postcode should be "SP14AS"
    And the postal area should be "SP"
    And the house number should be "742"
    And the street should be "Evergreen Terrace"
    And the town should be "Springfield"

  Scenario: Parse dob
    Given Some valid json
    When I parse the data
    Then the year of birth should be "1960"

  Scenario: Parse friends
    Given Some valid json
    When I parse the data
    Then the friends should be
      | Name   |
      | Moe    |
      | Barney |

  Scenario: Parse brand preferences
    Given Some valid json
    When I parse the data
    Then the brand preferences should be
      | Name         | Type |
      | Duff         | Beer |
      | Moe's Tavern | Bar  |

  Scenario: Parse family
    Given Some valid json
    When I parse the data
    Then the family should be
      | Name          | Relationship  |
      | Marge Simpson | Wife          |
      | Bart Simpson  | Child         |
      | Lisa Simpson  | Child         |
      | Abe Simpson   | Father        |
      | Selma Bouvier | Sister-In-Law |
      | Patty Bouvier | Sister-In-Law |

  Scenario: Parse performance review
    Given Some valid json
    When I parse the data
    Then the average score should be "1"
