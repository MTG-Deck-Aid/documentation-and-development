# SENG 401 PROJECT Testing Document
### Members
Sachin Seizer, Brendan SMILEY, Luca Rios, Cody Casselman, Rohan Lange and Wade Banman

# Introduction

For our application, the following systems are considered to be critical:
- [Database Connection](#Database-connection) (including create/read/update/delete)
- [Large Language Model querying](#LLM-Connector)
- [ScryFall API querying](#scryfall-connector)
- [User login Authenticaion](#authentication-system)
- [Frontend-backend connection](#frontend-to-backend-apis)

While not as critical, a test suite for frontend navigation was done as well to ensure user experience was smooth while using our application.

# Test Results

## Database Connection

### Test Results

<img src = "media\connector-tests.jpg" width = "720">

The databases connector is comprised of three classes:
- DatabaseConnector - the class responsible for the actual connection to the database and execution of queries
- CardQueries - class responsible for formatting queries for the card table
- DeckQueries - class responsible for formatting queries for the deck table

### Test Datasets

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

Force each class, weak Equivalence class testing (ECT) and Boundary Value Testing (BVT) was used to develop test cases.  This meant:

- Test with valid inputs
- Test with inputs right at the boundary of validity
- Test with error inputs


#### DatabaseConnector:

The main aspects to be tested:
1. Being able to connect to the database
2. Allowing only one instance of the class (to ensure single point of connection to database)

Test coverage:
1. TC-DC01, TC-DC03
2. TC-DC02

#### CardQueries:

The main aspects to be tested:
1. Insertion of rows
2. Reading of rows
3. Update of rows
4. deletion of rows

Test coverage:
1. TC-CQ01 - TC-CQ08
2. TC-CQ09, TC-CQ10
3. TC-CQ11 - TC-CQ16
4. TC-CQ17 - TC-CQ23

#### DeckQueries

The main aspects to be tested:
1. Insertion of rows
2. Reading of rows
3. Update of rows
4. deletion of rows

Test coverage:
1. TC-DQ01 - TC-DQ05
2. TC-DQ06 - TC-DQ09
3. TC-DQ10 - TC-DQ13
4. TC-DQ14 - TC-DQ16

## Frontend to Backend APIs

# TODO

### Test Results

### Test Datasets

### Test Validation


## LLM Connector

### Test Results

# TODO - get a screenshot of the tests running successfully

There are two main aspects of the AI connector to test: Getting suggestions on cards to remove, and getting suggestions on cards to add.  

### Test Datasets

The following dataset is a sample of a list of cards that would be passed to the LLM for processing

    {
    "num_to_add": 1,
    "num_to_remove": 2,
    "decklist": {
        "commander": "Marchesha The Black Rose",
        "mainboard": [
        {
            "name": "Ashnod's Al",
            "quantity": 1
        },
        {
            "name": "Demonic Tut",
            "quantity": 1
        },
        {
            "name": "Counterspell",
            "quantity": 1
        },
        {
            "name": "Sol Ring",
            "quantity": 1
        },
        {
            "name": "Swamp",
            "quantity": 9
        },
        {
            "name": "Island",
            "quantity": 9
        },
        {
            "name": "Mountain",
            "quantity": 12
        }
        ]
    }
    }


## Test Validation

Test validation for this method requires quantitative and qualitative analysis.  For the quantitative analysis, we need to validation that the AI returns the information in the required format.  An example can be seen [here](./media/prompt.txt).  The following test cases cover either the common cases or error cases expected from the LLM.

Common cases:
- TC-CS01, TC-CS02, TC-CS04, TC-CS05, TC-CS06
Error cases:
- TC-CS03

In terms of qualitative analysis, in regard to whether the quality of the suggestion is accurate, needs to be done manually.  After testing with various real life decks and comparing the suggestions of the LLM with reputable sources such as EDHRec and Moxfield, we can assert that the AI is giving accurate suggestions.

## Scryfall Connector

### Test Results

<img src = "media\scryfall-tests.jpg" width = "720">

### Test Datasets

test datasets would include the full/partial names of magic the gathering cards. such as:

    "Demonic Tutor"
    "Demonic"
    ""

### Test Validation

The ScryFallEngine class has one function to test.  Can it send and receive data from the ScryFall API.  Tests TC-SE01 and TC-SE02 
test the commmon and boundary cases for the class.  We can validate the correctness of the reponse by whether the response of the API was what was intended be received.  In the example of an input of "Demonic" this is an incomplete card name for the full card name "Demonic Tutor".  If the API returns "Demonic Tutor" the test passes.

## Authentication system

# TODO


### Test Results

### Test Datasets

### Test Validation


## Frontend Navigation

### Test Results

### Test Datasets

For testing the website, a deck from Moxfield will be used as sample data, as this is the mostly likely source where users using our website will get their data from.  The deck used for testing can found [here](https://moxfield.com/decks/SE4kNjfWsUy3bgm61p3-vQ).  The sideboard data is ignored as that is not relevant to the testing.

### Test Validation

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

These tests are all designed with covering the possible ways the user will interact with the website.  Selenium mimics the actions a human user would take while they're on the website.  With that knowledge, if the Selenium tests are able to succeed, we can be confident that a user would be able to do the same, validating the functionality of the website.