# Assessment-3-
Assessment 3: Programming Principles and Concepts






## Repository Overview 

This repository demonstrates software design principles through comprehensive analysis of a membership management system. The code examples showcase both successful principle applications and areas requiring improvement, providing insight into real-world software development challenges. Through detailed commentary and critical evaluation, this repository illustrates the practical application of fundamental programming concepts learned throughout the course.


## Code Analysis: Membership Management System

## Project Description
Project Description
The day3_lab.py file contains a console-based membership system for Whitecliffe Students Club, handling member registration, withdrawal, display, and search functionality. This system manages student club memberships through a menu-driven interface, validating student credentials, generating unique membership IDs, and maintaining accurate statistics about club membership.


## Software Design Principles Analysis
## (Successfully Implemented Principles)

**Single Responsibility Principle**
Each method has one clear job: register_member() only handles registration, display_members() only shows data
Makes code easier to understand and maintain
Allows independent testing and modification of each function

**Separation of Concerns**  
UI logic (main_menu) separated from business logic (register/withdraw operations)
Data operations separated from display operations
This architectural decision improves maintainability and allows for future interface changes

**K.I.S.S (Keep It Simple, Stupid)**
Uses simple data structures (dictionaries, lists) instead of complex objects
Clear variable names and straightforward control flow
Reduces cognitive load and makes code accessible to other developers

**Clean Code > Clever Code**
Readable method names and clear logic flow
Simple algorithms without unnecessary complexity
Prioritizes maintainability over performance optimization

**Composition > Inheritance**
Class contains member data as attributes rather than inheriting from parent class
Uses "has-a" relationship with member data
Provides flexibility and avoids complex inheritance hierarchies

**Y.A.G.N.I (You Ain't Gonna Need It)**
Implements only required functionality without over-engineering
No speculative features or unused complexity
Focuses development effort on actual requirements




## (Areas Requiring Improvement)

**D.R.Y (Don't Repeat Yourself) - Major Violations**
Search logic duplicated in withdraw_member() and show_member_details()
Programme counting logic repeated between registration and withdrawal
**Solution:** Extract find_member() and update_programme_count() methods to centralize common functionality

**Open/Closed Principle**
Hard-coded programme types make extension difficult
Adding new programme types requires modifying existing code
**Solution:** Use constants or enums for programme types to allow extension without modification

**Refactor, Refactor, Refactor**
Multiple areas need refactoring to eliminate code duplication
Improved structure would enhance long-term maintainability
**Solution:** Extract common functionality into helper methods and create reusable components



## Conclusion
This analysis demonstrates both successful applications of design principles (Single Responsibility, Separation of Concerns, K.I.S.S) and areas needing improvement (D.R.Y violations, refactoring opportunities). The membership system provides a clear example of how design principles improve code maintainability while highlighting real-world challenges in applying these concepts consistently.
Through this exercise, I have developed a deeper understanding of how theoretical design principles translate into practical coding decisions. Identifying both strengths and weaknesses in my code has enhanced my ability to write more maintainable, extensible software. The exercise has strengthened my critical code evaluation skills and demonstrated the importance of continuous refactoring in professional programming practice.
