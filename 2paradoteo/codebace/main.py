from basketball_league import BasketballLeague
from json_operations import JSONOperations


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
                league.exchange_players() 
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
        flag2 = True
        while flag2:
            print("\nChoose an option:")
            print("1. Show team averages")
            print("2. Show total team statistics")
            print("3. Show MVP")
            print("4. Show a Player's statistics")
            print("5. Back to main menu")
            option = input("Enter the option number (1/2/3/4/5): ")
            if option == "1":
                league.calculate_averages()
                flag2 = False
                flag1 = False
            elif option == "2":
                league.show_total_team_statistics()
                flag2 = False
            elif option == "3":
                league.show_MVP()
            elif option == "4":
                league.show_player_statistics()
            elif option == "5":
                flag2 = False
    elif option == "7":
        exit()
    else:
        print("Invalid option. Please enter 1, 2, 3, 4, 5, 6, or 7")




# Append to the JSON file
file.append_to_json_file(league)

