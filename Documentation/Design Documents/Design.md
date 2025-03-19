# SENG 401 PROJECT Design Document
### Members
Sachin Seizer, Brendan SMILEY, Luca Rios, Cody Casselman, Rohan Lange and Wade Banman

# Well Defined Structure of Project

...class diagrams

# Use of Design Patterns

In our project we made use of a few design patterns.

DatabaseConnector - Singleton

As part of our functional requirements of having a single point of access to the database, the DatabaseConnector class
was built using a Singleton design pattern.  This design pattern was chosen as by only allowing one instance of the 
DatabaseConnector class to exist, then by consequence only one connection to the database can exist.

CardSuggestor - Strategy

As part of the strategy to keep our project scalable and adaptable to the future, we implemented the CardSuggestor class
with the Strategy design pattern.  Here, the strategy is what Large Language Model (LLM) is to be used for the card suggestions.
This choice was made to allow for easy changin of which kind of LLM our project would use.  This is important as years down the line
new, better LLMs may be released or the exisiting LLM we're using (currently the Gemini AI) may become inneffective or taken down.  
With the strategy pattern, we can easily create a new strategy using a different AI without have to change any existing code, adhering
to the open-close principle.

??? - Decorator


# Adherance to SOLID Principles

In our project we made lots of effort to adhere our programming to the SOLID principles.  Here I will list how we did so for each principle.

S - Single Responsibility

The database connection classes are a good example of adherance to single responsibility.  In the Database_Connector folder, there are three classes: 
DatabaseConnector, CardQueries, DeckQueries.  Each of these classes is responsible for a single job.  DatabaseConnector sends queries to the database, CardQueries builds queries for the Card table and Deckqueries builds queries for the Deck table.  

We also have other examples of classes that have only responsibility, such as the ScryFallEngine class that focuses solely on communication information with the ScryFall API.

O - Open-Close Principle

Our CardSuggestor class follows the Open-Close Principle.  By using the Strategy pattern, whenever a new LLM needs to be used, we can simply 
create a new strategy instead of having to modify the existing methods.

L - Liskov Subtitution

I - Interface Seggregation

D - Dependency Inversion

