# SENG 401 PROJECT Requirements Document
### Members
Sachin Seizer, Brendan SMILEY, Luca Rios, Cody Casselman, Rohan Lange and Wade Banman


# Functional Requirments

- Connect to a PostGreSQL database
- create/read/update/delete deck and card data to database
- maintain a single point of access to the database
- Authenticate users
- Keep private user data secure
- Use a generative AI to analyse the user inputted decks and get deck tuning suggestions
- Communicate with ScryFall API to get magic card information
- Website must be able to run on both mobile devices and desktops
- users can login
- users can use the application as a guest 

# Non Functional Requirements
- Requests to Scryfall API are structured so that the request is processed in a reasonable amount of time.
- Requests to Gemini API are structure so that the response is easy for the user to understand
- UI of frontend webpage is made to be intuitive for the user to navigate
- Database queries are structured to be completed in a reasonable amount of time
- User authentication tokens are verified on both ends to ensure security

# User Stories
## Guest Users

As a guest user I want to be able to paste in my deck and get suggestions so that I can quickly figure out what changes I should make to my deck

As a guest user I want to be free to navigate the website without have to login so that I can still easily make use of the website's features.

## Registered Users

As a registered user I want to be able to save my inputted decks so that I can review them again later.

As a registered user I want to be able to have multiple decks saved at once so that I have flexibility on which deck I would like to work on on a given date.

As a registered user I want to be able to easily sign in and out of my account so that I can feel secure that my account won't be accessed by others.

## General Users

As a user I want to be able to get relevant suggestions on any of my decks so that I can improve my decks.

As a user I want to be able to be able to chose which suggestions to apply to my deck and have it done automaticlaly to make tuning my deck much easier.

As a user I want the ability to import my decks from any of the common deck building websites, such as Moxfield, to simplify the process of having my deck tuned.

# Requirements Traceability Matrix

| Requirement ID    | Requirement Description   | Design Reference  | Test Case ID  | Status    |
| ----------------- | ------------------------- | ----------------- | ------------- | --------- |
| REQ - 01          | User must be able to visit the home page |                   |               | Completed/Needs Testing          |
| REQ - 02          | User must be able to sign up |                   |               | Completed/Needs Testing          |
| REQ - 03          | User must must be able to login using an existing account |                   |               | Completed/Needs Testing          |
| REQ - 04          | User must be able to create a new deck |                   |               | Completed/Needs Testing          |
| REQ - 05          | A logged in user must be able to view their existing decks |                   |               | In Progress          |
| REQ - 06          | A logged in user must be able to edit their existing decks |                   |               | In Progress          |
| REQ - 07          | A user must be able to copy paste in their deck list from commonly used websites such as Moxfield |                   |               | Completed/Needs Testing          |
| REQ - 08          | A user must be able to get suggestions on cards to add/remove from their pasted in deck |                   |               | Completed/Needs Testing          |
| REQ - 09          | A logged in user must be able to log out |                   |               | Completed/Needs Testing          |
| REQ - 10          | The backend must be able to connect to the database |                   | TC-DC01-02              | Completed          |
| REQ - 11          | The backend must be able to insert into card table |                   | TC-CQ01-08              | Completed           |
| REQ - 12          | The backend must be able to read from card table |                   | TC-CQ09-10              | Completed          |
| REQ - 13          | The backend must be able to delete from card table |                   | TC-CQ17-23              | Completed          |
| REQ - 14          | The backend must be able to update from card table |                   | TC-CQ11-16              | Completed          |
| REQ - 15          | The backend must be able to insert into deck table |                   | TC-DQ01-05              | Completed          |
| REQ - 16          | The backend must be able to read from deck table |                   | TC-DQ06-09              | Completed          |
| REQ - 17          | The backend must be able to delete from deck table |                   | TC-DQ14-16              | Completed          |
| REQ - 18          | The backend must be able to update from deck table |                   | TC-DQ10-13              | Completed          |
| REQ - 19          | The backend must be able to connect to scryfall API |                   | TC-SE01-02              | Completed          |
| REQ - 20          | The backend must be able to find a partially inputted card name using scryfall API |                   | TC-SE01              | Completed          |
| REQ - 21          | The backend must be able to validate a user inputted deck list in less than 5 seconds |                   |               | Needs Testing          |
| REQ - 22          | The backend must be able to connect to the Gemini API |                   | TC-CS01-06              | Completed          |
| REQ - 23          | The backend must be able to get 1-5 suggestions on cards to add to the deck from the Gemini API |                   | TC-CS02, TC-CS05              | Completed          |
| REQ - 24          | The backend must be able to get 1-5 suggestions on cards to remove from the deck from the Gemini API |                   | TC-CS04              | Completed          |
| REQ - 25          | User must be able to click a button to automatically apply the AI suggestions that they wish to apply |                   |               | Not Started          |
| REQ - 26          | The User must be able to search for their commander and get real time autofill suggestions |                   |               | Needs Testing          |
| REQ - 27          | Frontend must be able to request and retrieve an authentication token from auth0                          |                   |               | In Progress          |
| REQ - 28          | The backend must be able to validate authentication tokens sent back by the frontend                          |                   |               | In Progress          |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |
|                   |                           |                   |               |           |