# SENG 401 PROJECT Requirements Document
### Members
Sachin Seizer, Brendan SMILEY, Luca Rios, Cody Casselman, Rohan Lange and Wade Banman

# Functional Requirments

#### Here's a list of the functional requirements of our system:
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
