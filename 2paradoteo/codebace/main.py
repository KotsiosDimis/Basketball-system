from tkinter import S
from basketball_league import BasketballLeague
from json_operations import JSONOperations
import os


class BasketballApp:
    def __init__(self):
        # Check if the JSON file exists
        if os.path.exists('2paradoteo\\codebace\\basketball_data.json'):
            # If the file exists, load the existing teams from the file
            self.file = JSONOperations(
                '2paradoteo\\codebace\\basketball_data.json')
            existing_teams = self.file.handle_json()
            # Initialize the league with the existing teams
            self.league = BasketballLeague(existing_teams)
            self.datanotfound = False
        else:
            # If the file does not exist, create a new file and initialize an empty league
            print(
                "\nDatabase not found. Create new data using the Append new data option.")
            self.file = JSONOperations(
                '2paradoteo\\codebace\\basketball_data.json')
            self.league = BasketballLeague([])

            self.datanotfound = True

    def run(self):
        
        while self.datanotfound:
            print("\nChoose an option:\n")
            print("\t1. Append new data")
            print("\t2. Exit")
            option = input("\nEnter the option number (1/2): ")
            if option == "1":
                # Append new teams to the league
                self.league.append_new_teams()
                self.datanotfound = False
            elif option == "2":
                # Exit the program
                choice = input(
                    "\nAre you sure you want to exit? If yes, type 'y': ")
                if choice.lower() == "y":
                    print("\nThanks for using our program!\n")
                    exit()
            else:
                print("\nInvalid option. Please try again.")
        while True:
            print("\nChoose an option:\n")
            print("\t1. Use existing data")
            print("\t2. Append new data")
            print("\t3. Reset all values to 0")
            print("\t4. Delete all existing data and start fresh")
            print("\t5. Update Roster")
            print("\t6. Show Stats")
            print("\t7. Exit")
            option = input("\nEnter the option number (1/2/3/4/5/6/7): ")

            if option == "1":
                # Create a championship using existing data
                self.league.create_championship()
                break
            elif option == "2":
                # Append new teams to the league
                self.league.append_new_teams()
            elif option == "3":
                # Reset all numerical values to 0 in the JSON file
                self.file.reset_numerical_values()
            elif option == "4":
                # Delete all data in the JSON file and exit
                self.file.delete_data()
                exit()
            elif option == "5":
                # Navigate to the update roster menu
                self.update_roster()
            elif option == "6":
                # Navigate to the show stats menu
                self.show_stats()
            elif option == "7":
                # Confirm exit or return to the main menu
                choice = input(
                    "\nAre you sure you want to exit? If yes, type 'y': ")
                if choice.lower() == "y":
                    print("\nThanks for using our program!\n")
                    exit()
            else:
                print("Invalid option. Please enter 1, 2, 3, 4, 5, 6, or 7")

    def update_roster(self):
        flag = True  # Set a flag to True to start the loop
        while flag:  # Loop until the flag is False
            print("\nChoose an option:\n")  # Display menu options
            print("\t1. Exchange players")
            print("\t2. Add new players")
            print("\t3. Remove players")
            print("\t4. Back to main menu")
            # Get user input
            option = input("\nEnter the option number (1/2/3/4): ")
            if option == "1":  # If option is 1
                # Exchange players between teams
                self.league.exchange_players()
            elif option == "2":  # If option is 2
                # Add new players to a team
                self.league.add_new_players()
            elif option == "3":  # If option is 3
                # Remove players from a team
                self.league.remove_players()
            elif option == "4":  # If option is 4
                flag = False  # Set flag to False to exit the loop

    def show_stats(self):
        # Initialize flag to True
        flag = True

        # Continue the loop until flag is False
        while flag:
            # Display the menu options
            print("\nChoose an option:\n")
            print("\t1. Show team averages")
            print("\t2. Show total team statistics")
            print("\t3. Show MVP")
            print("\t4. Show a Player's statistics")
            print("\t5. Back to main menu")

            # Prompt the user to enter an option number
            option = input("\nEnter the option number (1/2/3/4/5): ")

            # Check the option selected by the user
            if option == "1":
                # Calculate and show team averages
                self.league.calculate_averages()
            elif option == "2":
                # Show total team statistics
                self.league.show_total_team_statistics()
            elif option == "3":
                # Show MVP of the tournament
                self.league.show_MVP()
            elif option == "4":
                # Show statistics for a specific player
                self.league.show_player_statistics()
            elif option == "5":
                # Set flag to False to exit the loop
                flag = False


if __name__ == "__main__":
    # Instantiate the BasketballApp and run the application
    app = BasketballApp()
    app.run()
