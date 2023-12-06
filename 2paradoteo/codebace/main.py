from basketball_league import BasketballLeague
from json_operations import JSONOperations
import os

# Instantiate the league outside the loop
league = BasketballLeague([])
file = JSONOperations('2paradoteo\\codebace\\basketball_data.json')

while True:
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
        if os.path.exists('basketball_data.json'):
            existing_teams = file.handle_json()
            league.teams.extend(existing_teams)
            league.create_championship()
            break
        else:
            print("Error: 'basketball_data.json' not found. Please choose option 2 or 3.")
    elif option == "2":
        existing_teams = file.handle_json()  # Read existing teams from JSON
        current_team_count = len(existing_teams)
        print("To maintain a balanced championship, the total number of teams must be even.")
        if current_team_count % 2 == 0:
            print(f"Currently, there are {current_team_count} teams, which is even. You need to add an even number of new teams to keep the total even.")
        else:
            print(f"Currently, there are {current_team_count} teams, which is odd. You need to add an odd number of new teams to make the total even.")
        num_teams_to_add = int(input("Enter the number of new teams you want to add: "))
        while (current_team_count + num_teams_to_add) % 2 != 0:
            if num_teams_to_add % 2 == 0:
                print("You've entered an even number of new teams which would result in an odd total. Please enter an odd number of new teams.")
            else:
                print("You've entered an odd number of new teams which would still result in an odd total. Please enter an even number of new teams.")
            num_teams_to_add = int(input("Enter a different number of teams to add: "))
        league.create_teams(num_teams_to_add)
        
        num_players_per_team = int(input("\nEnter the number of players per team (between 5 and 10): "))
        while num_players_per_team < 5 or num_players_per_team > 10:
            print("Invalid number of players. There must be between 5 and 10 players per team.")
            num_players_per_team = int(input("Please enter the number of players per team (between 5 and 10): "))

        for team in league.teams:
            league.create_players_for_team(team, num_players_per_team)
        existing_teams = file.handle_json()
        league.teams.extend(existing_teams)
        break
    elif option == "3":
        file.reset_numerical_values()
    elif option == "4":
        file.delete_data()
        exit()
    elif option == "5":
        exit()
    else:
        print("Invalid option. Please enter 1, 2, 3, 4 or 5")

# Start the championship


# Append to the JSON file
file.append_to_json_file(league)
