#part 1

class Membership:
    def __init__(self):
        self.members = []  # List of members
        self.total_members = 0
        self.diploma_members = 0
        self.bachelor_members = 0
        self.withdrawn_members = 0

#part 2

    def register_member(self):
        student_id = input("Enter Student ID: ")
        last_name = input("Enter Last Name: ")
        programme = input("Enter Programme (Diploma/Bachelor): ")
        
        # Check if Student ID starts with W
        if not student_id.startswith("W"):
            print("Error: Only Whitecliffe students can join!")
            return
        
        # Create membership ID (WCSC1, WCSC2, etc.)
        membership_id = f"WCSC{self.total_members + 1}"
        
        # Create member dictionary
        member = {
            "membership_id": membership_id,
            "student_id": student_id,
            "last_name": last_name,
            "programme": programme
        }
        
        # Add to list
        self.members.append(member)
        self.total_members += 1
        
        # Update programme counts
        if programme == "Diploma":
            self.diploma_members += 1
        elif programme == "Bachelor":
            self.bachelor_members += 1
            
        print(f"Success! {last_name} registered with ID: {membership_id}")


#part 3

    def withdraw_member(self):
        membership_id = input("Enter Membership ID: ")
        last_name = input("Enter Last Name: ")
        
        # Look for the member
        for member in self.members:
            if member["membership_id"] == membership_id and member["last_name"] == last_name:
                # Found the member - remove them
                self.members.remove(member)
                self.total_members -= 1
                self.withdrawn_members += 1
                
                # Update programme counts
                if member["programme"] == "Diploma":
                    self.diploma_members -= 1
                elif member["programme"] == "Bachelor":
                    self.bachelor_members -= 1
                    
                print(f"Success! {last_name} has been withdrawn.")
                return
        
        # If we get here, member not found
        print("Error: Member not found!")

# part 4

    def display_members(self):
        print("\n--- All Members ---")
        for member in self.members:
            print(f"ID: {member['membership_id']}, Student: {member['student_id']}, Name: {member['last_name']}, Programme: {member['programme']}")
        
        print("\n--- Statistics ---")
        print(f"Total members: {self.total_members}")
        print(f"Diploma students: {self.diploma_members}")
        print(f"Bachelor students: {self.bachelor_members}")
        print(f"Withdrawn members: {self.withdrawn_members}")


#part 5

    def show_member_details(self):
        membership_id = input("Enter Membership ID: ")
        
        for member in self.members:
            if member["membership_id"] == membership_id:
                print(f"Membership ID: {member['membership_id']}")
                print(f"Student ID: {member['student_id']}")
                print(f"Last Name: {member['last_name']}")
                print(f"Programme: {member['programme']}")
                return
        
        print("Error: Member not found!")


#part 6

    def main_menu(self):
        while True:
            print("\n--- Whitecliffe Students Club ---")
            print("1. Register a new member")
            print("2. Withdraw a member")
            print("3. Display all members and statistics")
            print("4. Show specific member details")
            print("5. Quit the system")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
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

club = Membership()
club.main_menu()