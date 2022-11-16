
# Information about the program.

# The user interface shall be row-oriented and executed in the command shell.
# The user interface shall consist of different menu options. The menu options
# shall be possibly to use in an arbitrary order. One option has to be for
# quitting the program. 
import team

teams:list[str]=[]                   
restored_teams:list[str]=[]                   


class User_interface:
    #obj = team.Team("björnarna", "girls", True, 2200)        # Checks if it works to create
    #print(obj)                                                 #  objects from the imported class  

    quit = 12                                                   # Quit variable to end the while loop.             

# Creates a menu option with 12 alternatives for the user to choose between.

def display_menu():
    print(' MENU')
    print('Write everything with lowercase! you must spell correctly for the program to understand what you mean.')
    print('1) Add another team')
    print('2) Select a team based on the id to show their information')
    print('3) List all of the boys/girls team and show information')
    print('4) List all teams regardless of gender')
    print('5) Update the fields of a team')
    print('6) Delete a selected team')
    print('7) Print out how many teams that exist at the moment: ')
    print('8) Print out how how many percent of all teams that has paid their fee')
    print('9) Type in the name of a team that has cancelled their participation')
    print('10) Store the information about all the teams to a text file')
    print('11) Restore the content of all the teams to the program, from a text file (need to choose option 10 first)')
    print('12) Exit')
    
def main():
    choice = 0                                       # Will be set to the users choise in the menu options.
    
    while choice != quit:
        display_menu()                              # Show all the options to the user.
        choice = int(input('Enter your choice (1-12): '))

        # A menu option to add new teams. Askes the user for all information about the new team.
        if choice == 1:
            name = str(input('Enter the name of the team: '))           
            type_ = str(input('Enter boys or girls: '))
            fee_paid = str(input('Enter if the fee has been paid or not (yes/no): '))
            fee = int(input('Enter the fee each team must pay to participate: '))
            new_team = team.create_team(name, type_, fee_paid, fee)
            teams.append(new_team)
            print(new_team.get_id())
            print(new_team.get_date())
          

        # A menu option for selecting a team, based on the id, and show all
        # information about the selected team

        elif choice == 2:
            id_ = int(input('Enter the id for the team you want to select: '))       
            for i in range(0,len(teams)):
                if id_ == teams[i].get_id():
                    print(f"Name: {teams[i].get_name()} Id:{teams[i].get_id()} Date: {teams[i].get_date()} Gender: {teams[i].get_type_()} Fee: {teams[i].get_fee()} Fee paid: {teams[i].get_fee_paid()} Cancellation: {teams[i].get_cancellation()}")
                else:
                    break

        # A menu option to list all teams for boys or girls and show all information
        # about the teams in a clear way

        elif choice == 3:
            gender = str(input('Enter if you want to select boys or girls (boys/girls): '))
            for i in range(0,len(teams)):
                if teams[i].get_type_() == gender:                         # Compares the users choise to all types in the list.
                    print(f"Name: {teams[i].get_name()} Id:{teams[i].get_id()} Date: {teams[i].get_date()} Gender: {teams[i].get_type_()} Fee: {teams[i].get_fee()} Fee paid: {teams[i].get_fee_paid()} Cancellation: {teams[i].get_cancellation()}")
                else:
                    continue
                
        # A menu selection to list all teams, regardless of team type, and display
        # all information about the teams in a clear way
        
        elif choice == 4:                                              
            for i in range(0,len(teams)):                   
                    print(f"Name: {teams[i].get_name()} Id:{teams[i].get_id()} Date: {teams[i].get_date()} Gender: {teams[i].get_type_()} Fee: {teams[i].get_fee()} Fee paid: {teams[i].get_fee_paid()} Cancellation: {teams[i].get_cancellation()}")


        # Update the fields of a team from a particular menu option, except the id
        # and date make sure it’s easy for the user to choose an existing team in the program

        elif choice == 5:
                update = str(input('Type in the name of the team you want to update information for: '))
                for i in range(0,len(teams)):
                    if teams[i].get_name() == name:                                     # Compares the users choise to all types in the list.
                        name = str(input('Enter the new name of the team: '))          
                        type_ = str(input('Enter boys or girls: '))
                        fee_paid = str(input('Enter if the fee has been paid or not (yes/no): '))
                        fee = int(input('Enter the fee each team must pay to participate: '))
                        teams[i].set_name(name)
                        teams[i].set_type_(type_)
                        teams[i].set_fee_paid(fee_paid)
                        teams[i].set_fee(fee)


        # Delete a selected team by a particular menu option o make sure it’s easy
        # for the user to choose a team.
        
        elif choice == 6:
            name = str(input('Type in the name of the theam you want to delete: '))     
            for i in range(0,len(teams)):
                if teams[i].get_name() == name:                                         # Compares the users choise to all types in the list.
                    teams.remove(teams[i])
            print("Prints out the names of the teams that are left.")
            for i in range(0,len(teams)):                   
                    print(f"Name: {teams[i].get_name()}")


        # By using one menu option show how many teams that exists, at the moment.
        
        elif choice == 7:
            print(f"The number of teams in the list equals: {len(teams)}")


        # By using one menu option how many percent of all teams that has paid their fee.
        
        elif choice == 8:
            counter_fee_paid = 0                  # Counter for finding the percentage.

            for i in range(0,len(teams)):
                if teams[i].get_fee_paid() == "yes":
                    counter_fee_paid = counter_fee_paid + 1
                else:
                    continue
                print(f"{counter_fee_paid/len(teams)} percentage of the teams has paid." )              # Find the percentage.

        # If a team has cancelled their participation, show this by adding a date.
        
        elif choice == 9:
            name = str(input('Type in the name of the team that is calncelled: '))
            cancellation = str(input('What is the cancellation date (use the format YYYY-MM-DD): '))
            for i in range(0,len(teams)):
                    if teams[i].get_name() == name:        
                        teams[i].set_cancellation(cancellation)
                        print(f"Cancellation date for the " f"team {teams[i].get_name()}" f" is: {teams[i].get_cancellation()}")
                    else:
                        print("The team is not reported")
                        continue


        # File handeling.
        # Store the information about all the teams to a text file. It has to be in a text
        # file with file extension .tx
        
        elif choice == 10:
            with open('teams.txt', 'w') as f:
                 for i in range(0,len(teams)):                      
                    f.write(f"{teams[i].get_name()}"+"\n"+f"{teams[i].get_date()}"+"\n"+f"{teams[i].get_id()}"+"\n"+f"{teams[i].get_type_()}"+"\n"+f"{teams[i].get_fee()}"+"\n"+f"{teams[i].get_fee_paid()}"+"\n"+f"{teams[i].get_cancellation()}"+"\n")
                    #print(f"{teams[i].get_name()}"+"\n"+f"{teams[i].get_date()}"+"\n"+f"{teams[i].get_id()}"+"\n"+f"{teams[i].get_type_()}"+"\n"+f"{teams[i].get_fee()}"+"\n"+f"{teams[i].get_fee_paid()}"+"\n"+f"{teams[i].get_cancellation()}"+"\n")
                    print("The information has been stored to a text file.")
                    
        # File handeling
        
        # restore the content of all the teams to the program, with help of the same text file
        # after restoring the teams from the file, the program should be able to continue
        # running and it should be possible to add, view, update and delete teams
    
        elif choice == 11:
           
            restore:list[str]=[]
            teamFile = open("teams.txt","r")            # Open the txt file
            contents = teamFile.readlines()             # Read all the lines
            numb_of_teams = len(teams)                  # Calculates the number of teams.

            for i in range(0,7*len(teams)):            # Restore everything
                restore.append(contents[i])             # Add all information in a new list restore.

            for i in range(1,numb_of_teams+1):
                name = contents[i*0]                    # Finds all the correct information from the list 
                date_ = contents[i*1]                   # based index and the order of the information.
                id_ = contents[i*2]
                #print(id_)                             # For testing.
                type_ = contents[i*3]
                fee = contents[i*4]
                fee_paid = contents[i*5]
                cancellation = contents[i*6]
                new_object = team.create_team(name, type_, fee_paid, fee)            # Creates new object with characteristics from txt. 
                setattr(new_object, "__id", id_)
                setattr(new_object, "__date", date_)
                #print(new_object.__id)                  # For testing
                restored_teams.append(new_object)       # Saves all the created objects in a list.
                
            print("The file has been restored in the list called resteored_teams.")

                
                
        # Menu option to exit the program.

        elif choice == 12:
            print('Exiting the program.')                                
            break
        
        else:
            print('Error: invalid selection.')
            

# Runs the main function

if __name__ == "__main__":
    main()
    

