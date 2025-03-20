# SENG 401 PROJECT Testing Document
### Members
Sachin Seizer, Brendan SMILEY, Luca Rios, Cody Casselman, Rohan Lange and Wade Banman

# Test Results

Critical Systems: 
## Database connector

<img src = "media\connector-tests.jpg" width = "720">

The databases connector is comprised of three classes:
- DatabaseConnector - the class responsible for the actual connection to the database and execution of queries
- CardQueries - class responsible for formatting queries for the card table
- DeckQueries - class responsible for formatting queries for the deck table

### Test datasets:

DatabaseConnector - no data required

CardQueries:

    cards = [
        {'cardname': 'Card A', 'sideboard': False, 'cardtype': 'Creature', 'count': 3},
        {'cardname': 'Card B', 'sideboard': True, 'cardtype': 'Sorcery', 'count': 2},
        {'cardname': 'Card C', 'sideboard': False, 'cardtype': 'Instant', 'count': 4},
        {'cardname': 'Card D', 'sideboard': True, 'cardtype': 'Enchantment', 'count': 1}
        ]

DeckQueries:

    decks = [
        ["10", "Commander", "Deck1", "Card A"],
        ["10", "Commander", "Deck2", None],
        ["10", "Standard", "Deck3", None],
        ["20", "Commander", "Deck4", None],
        ["20", "Modern", "Deck5", None]
    ]

### Test Validation

#### DatabaseConnector:

The main aspects to be tested:
1. Being able to connect to the database
2. Allowing only one instance of the class (to ensure single point of connection to database)

Tests that cover that
1. TC-DC01, TC-DC03
2. TC-DC02

#### CardQueries:

The main aspects to be tested:
1. Insertion of rows
2. Reading of rows
3. Update of rows
4. deletion of rows

Tests that cover each:
1. TC-CQ01 - TC-CQ08
2. TC-CQ09, TC-CQ10
3. TC-CQ11 - TC-CQ16
4. TC-CQ17 - TC-CQ23

in each case, weak Equivalence class testing (ECT) and Boundary Value Testing (BVT) was used to develop test cases.  This meant:

- Test with valid inputs
- Test with inputs right at the boundary of validity (ex. count = 1)
- Test with error inputs (ex. count = -2)

#### DeckQueries

The main aspects to be tested:
1. Insertion of rows
2. Reading of rows
3. Update of rows
4. deletion of rows

Tests that cover each:
1. TC-DQ01 - TC-DQ05
2. TC-DQ06 - TC-DQ09
3. TC-DQ10 - TC-DQ13
4. TC-DQ14 - TC-DQ16


in each case, weak Equivalence class testing (ECT) and Boundary Value Testing (BVT) was used to develop test cases.  This meant:

- Test with valid inputs
- Test with inputs right at the boundary of validity
- Test with error inputs

## frontend to backend APIs


## AI connector

# TODO - get a screenshot of the tests running successfully

There are two main aspects of the AI connector to test: Getting suggestions on cards to remove, and getting suggestions on cards to add.  

Common Cases:
- TC-CS01, 02, 04, 05, 06

Error Cases:
- TC-CS03

## Scryfall connector

<img src = "media\scryfall-tests.jpg" width = "720">

The ScryFallEngine class has one function to test.  Can it send and receive data from the ScryFall API.  Tests TC-SE01 and TC-SE02 
test the commmon and boundary cases for the class.  

Common cases:
- TC-CS01, TC-CS02, TC-CS04, TC-CS05, TC-CS06
Error cases:
- TC-CS04

## Authentication system

## Frontend Navigation

We made use of selenium to perform various navigation and feature tests of the frontend.  The main aspects tested were:
1. basic navigation
2. login
3. editing a deck
4. getting suggestions
5. applying suggestions
6. Mobile navigation

for each, these are the tests the cover each one:
1. TC-FR01-02
2. TC-FR03
3. TC-FR04-06, TC-FR10-12, 14
4. TC-FR07, 13
5. TC-FR08
6. TC-FR09
