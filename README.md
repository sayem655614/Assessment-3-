# Assessment-3-
Assessment 3: Programming Principles and Concepts






## Repository Overview 

This repository demonstrates software design principles through analysis of a membership management system. The code examples show both successful principle applications and areas requiring improvement.


## Code Analysis: Membership Management System

## Project Description
The `day3_lab.py` file contains a console-based membership system for Whitecliffe Students Club, handling member registration, withdrawal, display, and search functionality.


## Software Design Principles Analysis
## (Successfully Implemented Principles)

**Single Responsibility Principle**
= Each method has one clear job: `register_member()` only handles registration, `display_members()` only shows data
= Makes code easier to understand and maintain

**Separation of Concerns**  
= UI logic (main_menu) separated from business logic (register/withdraw operations)
= Data operations separated from display operations

**K.I.S.S (Keep It Simple, Stupid)**
= Uses simple data structures (dictionaries, lists) instead of complex objects
= Clear variable names and straightforward control flow

**Clean Code > Clever Code**
= Readable method names and clear logic flow
= Simple algorithms without unnecessary complexity

**Composition > Inheritance**
= Class contains member data as attributes rather than inheriting from parent class
= Uses "has-a" relationship with member data

**Y.A.G.N.I (You Ain't Gonna Need It)**
= Implements only required functionality without over-engineering
= No speculative features or unused complexity




## (Areas Requiring Improvement)

**D.R.Y (Don't Repeat Yourself) - Major Violations**
= Search logic duplicated in `withdraw_member()` and `show_member_details()`
= Programme counting logic repeated between registration and withdrawal
= **Solution:** Extract `find_member()` and `update_programme_count()` methods

**Open/Closed Principle**
= Hard-coded programme types make extension difficult
= **Solution:** Use constants or enums for programme types

**Refactor, Refactor, Refactor**
= Multiple areas need refactoring to eliminate code duplication
= **Solution:** Extract common functionality into helper methods



## Conclusion
This analysis demonstrates both successful applications of design principles (Single Responsibility, Separation of Concerns, K.I.S.S) and areas needing improvement (D.R.Y violations, refactoring opportunities). The membership system provides a clear example of how design principles improve code maintainability while highlighting real-world challenges in applying these concepts consistently.
The exercise has enhanced my understanding of software design principles and developed critical code evaluation skills essential for professional programming.
