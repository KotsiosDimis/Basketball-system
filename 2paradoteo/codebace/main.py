from basketball_league import BasketballLeague
from json_operations import JSONOperations
import os

# Instantiate the league outside the loop

file = JSONOperations('2paradoteo\\codebace\\basketball_data.json')
existing_teams = file.handle_json()
league = BasketballLeague(existing_teams)

flag1=True
while flag1:
    print("\nChoose an option:")
    print("1. Use existing data")
    print("2. Append new data")
    print("3. Reset all values to 0")
    print("4. Delete all existing data and start fresh")
    print("5. Update Roster")
    print("6. Show Stats")
    print("7. Exit")
    option = input("Enter the option number (1/2/3/4/5/6/7): ")
    
    # TODO: Add option to make changes for players and teams
    if option == "1":
        league.create_championship()
        break
    elif option == "2":
        league.append_new_teams()
        break
    elif option == "3":
        file.reset_numerical_values()
    elif option == "4":
        file.delete_data()
        exit()
    elif option == "5":
        flag2=True
        while flag2:
            print("\nChoose an option:")
            print("1. Exchange players")
            print("2. Add new player")
            print("3. Remove player")
            print("4. Back to main menu")
            option = input("Enter the option number (1/2/3/4): ")
            if option == "1":
                existing_teams = league.exchange_players(existing_teams)                
                flag1 = False
                flag2 = False              
            elif option == "2":
                league.add_new_players()
                flag1 = False
                flag2 = False
            elif option == "3":
                league.remove_players()
                flag1 = False
                flag2 = False
            elif option == "4":
                flag2 = False
                
        
    elif option == "6":
        league.show_stats()
    elif option == "7":
        exit()
    else:
        print("Invalid option. Please enter 1, 2, 3, 4 or 5")

# Start the championship


# Append to the JSON file
file.append_to_json_file(league)
