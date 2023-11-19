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
    print("5. Exit")
    option = input("Enter the option number (1/2/3/4/5): ")
    
    # TODO: Add option to make changes for players and teams
    if option == "1":
        if os.path.exists('2paradoteo\\codebace\\basketball_data.json'):
            existing_teams = file.handle_json()
            league.teams.extend(existing_teams)
            break
        else:
            print("Error: 'basketball_data.json' not found. Please choose option 2 or 3.")
    elif option == "2":
        num_teams = int(input("Enter the number of teams that you want to add: "))
        league.create_teams(num_teams)
        num_players_per_team = int(input("\nEnter the number of players per team: "))
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
league.create_championship()

# Append to the JSON file
file.append_to_json_file(league)
