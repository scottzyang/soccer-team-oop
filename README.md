# Soccer Team OOP Project
<i>Scott Yang & Paul Fletes - ACS 1111</i>

This Python-based project is an exercise in exploring Object-Oriented Programming principles. 

The classes designed in the project were intended to show basic concepts, and not full functionality within an app. Various object attributes and methods contain
elements that one could incorporate in a game-like program that incorporated the use of managing athletes on a fantasty sports team. A better understanding of 
fantasy soccer can be found here: https://fantasy.mlssoccer.com/#help/game-rules.

## Project overview:

Our project was based around the idea of a base `Athlete` class that can be inherited from to form `Coaches` and `Players` for a soccer team. From there, we decided to inherit from 
the `Player` class to create `Attackers` and `Defenders`. Each class can instantiate example objects with class attributes and methods. 

To meet the requirement of one class demonstrating composition, we created the `Team` class that imports from `Player` to add players to a team, create a roster and take the field (eventually!)

## Demo & Diagram:
- View our 10 minute [demo video](https://youtu.be/E0Wr156g4MI).
- View our [UML Class Diagram](https://drive.google.com/file/d/1ECzKUt_XtWk0DvanENg1W5m6CzQ2mD0Y/view?usp=sharing).

## Assignment Requirements:

For this assignment you will need to complete the following requirements:

Classes:
- At **least** 4 classes are defined.
- At **least** 1 class demonstrates composition (being composed of other objects).
- At **least** 1 class inherits from another class.
- All classes are used to instantiate example objects.

Methods:

- Each class has at least 2 methods that use and/or modify class attributes.
- The subclass overrides at least one superclass method (this can be __init__ or another method).
- Rationale about which methods are private, protected, or public should be provided in code comments or verbally during presentation. 

Attributes:

- Each class has a least 2 instance attributes created in __init__()
- Rationale about which attributes are private, protected, or public should be provided in code comments or verbally during presentation. 

Diagram:

- A diagram is provided that shows an overview of all the classes that make up the system design
- Diagram shows relationships between classes.
- You can achieve this by creating UML Class Diagrams. Here is a template on how to make them, [here](https://docs.google.com/presentation/d/1OQ4Q3KV3MIuR_K7IKnnaJ2jGHv8NOeGpMbMhnFwJkbo/edit#slide=id.p1).

Presentation:
- 5 - 10 min video presentation that shows off your various classes. Recorded using Quick Time and uploaded to YouTube.




