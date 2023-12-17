from random import choice
from basketball_league import BasketballLeague
from json_operations import JSONOperations
import os


if os.path.exists('2paradoteo\\codebace\\basketball_data.json'):
    file = JSONOperations('2paradoteo\\codebace\\basketball_data.json')
    existing_teams = file.handle_json()
    league = BasketballLeague(existing_teams)
else:
    print("Database not found. Creating new data.")
    file = JSONOperations('2paradoteo\\codebace\\basketball_data.json')
    league = BasketballLeague([])


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

    if option == "1":
        league.create_championship()
        break
    elif option == "2":
        league.append_new_teams()
    elif option == "3":
        file.reset_numerical_values()
    elif option == "4":
        file.delete_data()
        exit()
    elif option == "5":
        flag = True
        while flag:
            print("\nChoose an option:")
            print("1. Exchange players")
            print("2. Add new players")
            print("3. Remove players")
            print("4. Back to main menu")
            option = input("Enter the option number (1/2/3/4): ")
            if option == "1":
                league.exchange_players()
            elif option == "2":
                league.add_new_players()
            elif option == "3":
                league.remove_players()
            elif option == "4":
                flag = False

    elif option == "6":
        flag = True
        while flag:
            print("\nChoose an option:")
            print("1. Show team averages")
            print("2. Show total team statistics")
            print("3. Show MVP")
            print("4. Show a Player's statistics")
            print("5. Back to main menu")
            option = input("Enter the option number (1/2/3/4/5): ")
            if option == "1":
                league.calculate_averages()
            elif option == "2":
                league.show_total_team_statistics()
            elif option == "3":
                league.show_MVP()
            elif option == "4":
                league.show_player_statistics()
            elif option == "5":
                flag = False
    elif option == "7":
        choice = input("Are you sure you want to exit? If yes, type 'y': ")
        if choice.lower() == "y":
            print("Thanks for using our program!")
            exit()

    else:
        print("Invalid option. Please enter 1, 2, 3, 4, 5, 6, or 7")
