# WHITECLIFFE STUDENTS CLUB MEMBERSHIP SYSTEM

#part 1

class Membership:  # SINGLE RESPONSIBILITY: This class only handles membership operations
    def __init__(self):
        self.members = []  # COMPOSITION > INHERITANCE: Contains data rather than inheriting
        self.total_members = 0
        self.diploma_members = 0
        self.bachelor_members = 0
        self.withdrawn_members = 0  # AVOID PREMATURE OPTIMISATION: Storing counters for efficiency

#part 2

    def register_member(self):  # SEPARATION OF CONCERNS: Only handles registration logic
        student_id = input("Enter Student ID: ")
        last_name = input("Enter Last Name: ")
        programme = input("Enter Programme (Diploma/Bachelor): ")
        
        # Check if Student ID starts with W
        if not student_id.startswith("W"):  # K.I.S.S: Simple validation check
            print("Error: Only Whitecliffe students can join!")
            return  # CLEAN CODE > CLEVER CODE: Early return is readable
        
        # Create membership ID (WCSC1, WCSC2, etc.)
        membership_id = f"WCSC{self.total_members + 1}"  # K.I.S.S: Simple string formatting
        
        # Create member dictionary
        member = {  # K.I.S.S: Simple data structure instead of complex objects
            "membership_id": membership_id,
            "student_id": student_id,
            "last_name": last_name,
            "programme": programme
        }
        
        # Add to list
        self.members.append(member)
        self.total_members += 1
        
        # Update programme counts
        if programme == "Diploma":  # DRY VIOLATION: This logic repeats in withdraw_member()
            self.diploma_members += 1
        elif programme == "Bachelor":
            self.bachelor_members += 1
            
        print(f"Success! {last_name} registered with ID: {membership_id}")


#part 3

    def withdraw_member(self):  # SINGLE RESPONSIBILITY: Only handles member withdrawal
        membership_id = input("Enter Membership ID: ")
        last_name = input("Enter Last Name: ")
        
        # Look for the member
        for member in self.members:  # DRY VIOLATION: Same search logic as show_member_details()
            if member["membership_id"] == membership_id and member["last_name"] == last_name:
                # Found the member - remove them
                self.members.remove(member)
                self.total_members -= 1
                self.withdrawn_members += 1
                
                # Update programme counts
                if member["programme"] == "Diploma":  # DRY VIOLATION: Repeats counting logic
                    self.diploma_members -= 1
                elif member["programme"] == "Bachelor":
                    self.bachelor_members -= 1
                    
                print(f"Success! {last_name} has been withdrawn.")
                return  # CLEAN CODE > CLEVER CODE: Clear exit point
        
        # If we get here, member not found
        print("Error: Member not found!")

# part 4

    def display_members(self):  # SINGLE RESPONSIBILITY: Only displays data, doesn't modify it
        print("\n--- All Members ---")
        for member in self.members:  # K.I.S.S: Simple loop without complex formatting
            print(f"ID: {member['membership_id']}, Student: {member['student_id']}, Name: {member['last_name']}, Programme: {member['programme']}")
        
        print("\n--- Statistics ---")
        print(f"Total members: {self.total_members}")  # Uses stored counters for efficiency
        print(f"Diploma students: {self.diploma_members}")
        print(f"Bachelor students: {self.bachelor_members}")
        print(f"Withdrawn members: {self.withdrawn_members}")


#part 5

    def show_member_details(self):  # SINGLE RESPONSIBILITY: Only shows individual member info
        membership_id = input("Enter Membership ID: ")
        
        for member in self.members:  # DRY VIOLATION: Same search pattern as withdraw_member()
            if member["membership_id"] == membership_id:
                print(f"Membership ID: {member['membership_id']}")  # CLEAN CODE > CLEVER CODE: Clear output format
                print(f"Student ID: {member['student_id']}")
                print(f"Last Name: {member['last_name']}")
                print(f"Programme: {member['programme']}")
                return
        
        print("Error: Member not found!")


#part 6

    def main_menu(self):  # SEPARATION OF CONCERNS: UI logic separate from business logic
        while True:  # Y.A.G.N.I: Simple loop, no over-engineering
            print("\n--- Whitecliffe Students Club ---")
            print("1. Register a new member")
            print("2. Withdraw a member")
            print("3. Display all members and statistics")
            print("4. Show specific member details")
            print("5. Quit the system")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":  # K.I.S.S: Simple if/elif instead of complex dispatch
                self.register_member()
            elif choice == "2":
                self.withdraw_member()
            elif choice == "3":
                self.display_members()
            elif choice == "4":
                self.show_member_details()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")



#part 7

club = Membership()  # CLEAN CODE > CLEVER CODE: Simple instantiation
club.main_menu()  # Y.A.G.N.I: No unnecessary complexity in program start
