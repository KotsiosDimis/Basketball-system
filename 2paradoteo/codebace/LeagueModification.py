from Roster import Roster
import json
from Player import Player


class LeagueModification(Roster):
    def __init__(self, teams):
        super().__init__(teams)


    def append_new_teams(self):
        # General try block to catch any unexpected exceptions
        try:
            # Get the current number of teams
            current_team_count = len(self.teams)

            # Prompt user based on whether current number of teams is even or odd
            if current_team_count % 2 == 0:
                print(f"\nCurrently, there are {current_team_count} teams, which is even. You need to add an even number of new teams to keep the total even.")
            else:
                print(f"\nCurrently, there are {current_team_count} teams, which is odd. You need to add an odd number of new teams to make the total even.")

            # Loop until user enters a valid number of new teams to add to make total even
            while True:
                try:
                    num_teams_to_add = int(input("\nEnter the number of new teams you want to add: "))

                    # Check if the new total will be even
                    if (current_team_count + num_teams_to_add) % 2 == 0:
                        break
                    else:
                        print("\nThe number of new teams must result in an even total. Please try again.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid integer.")

            print()
            # Create the new teams
            self.create_teams(num_teams_to_add)

            # Loop to get the number of players per team, must be between 5 and 10
            while True:
                try:
                    num_players_per_team = int(input("\nEnter the number of players per team (between 5 and 10): "))
                    if 5 <= num_players_per_team <= 10:
                        break
                    else:
                        print("\nInvalid range. Please enter a number between 5 and 10.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid integer.")

            print() 
            
            # Create players for the new teams
            for i in range(current_team_count, len(self.teams)):
                self.create_players_for_team(
                    self.teams[i], num_players_per_team)

            # Save the updated teams to a JSON file
            json.dump(self.teams_to_dict(self), open(
                '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

            # Try to save the updated teams to a JSON file, handle potential file not found error
            try:
                with open('2paradoteo\\codebace\\basketball_data.json', 'w') as file:
                    json.dump(self.teams_to_dict(self), file, indent=4)
            except FileNotFoundError:
                print("\nThe file path does not exist. Please check the path and try again.")
                
        except Exception as e:
            # Catch-all for any other exception that might occur
            print(f"\nAn error occurred: {e}")

    def exchange_players(self):
        try:
            # Display teams and prompt user to choose two teams
            print("\nChoose two teams to exchange players between:")

            # Choose the first team
            first_team = self.choose_team()
            print(f"\nChoose a player from {first_team.name}:")
            first_player = self.choose_player(first_team)

            # Choose the second team, excluding the first player's team
            second_team = self.choose_team(selected_team={first_team.name})
            print(f"\nChoose a player from {second_team.name}:")
            second_player = self.choose_player(second_team)

            # Exchange the players between the two teams
            first_team.players.remove(first_player)
            second_team.players.remove(second_player)
            first_team.players.append(second_player)
            second_team.players.append(first_player)

            # Print a message to indicate that players have been exchanged between the teams
            print(f"\nExchanged players between {
                  first_team.name} and {second_team.name}.")

            # Save the updated teams to a JSON file
            json.dump(self.teams_to_dict(self), open(
                '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

        except ValueError:
            # Handle case where user input is not an integer
            print("Error: Please enter a valid number.")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    def add_new_players(self):
        try:
            # Add a new player to a team
            team = self.choose_team()  # Choose a team to add players to

            if len(team.players) >= 10:  # Check if the team already has the maximum number of players
                # Print error message
                print(f"{team.name} already has the maximum number of players.")
                return  # Exit the function

            # Print current number of players in the team
            print(f"\nThere are currently {
                  len(team.players)} players in the team and the maximum is 10.")

            # Prompt user to enter the number of players to add
            num_of_players = int(
                input("\nEnter the number of players to add: "))

            # Check if the total number of players (existing + new) exceeds the maximum limit
            if len(team.players) + num_of_players > 10:
                print(f"{team.name} reached {len(
                    team.players) + num_of_players} players, which is more than the maximum of 10.")  # Print error message
                return  # Exit the function

            else:
                # Loop through the range of number of players to add
                for i in range(num_of_players):
                    # Prompt user to enter the name of the player
                    player_name = input(
                        f"\n\tEnter the name of player {i + 1}: ")

                    # Prompt user to enter the position of the player
                    player_position = input(
                        f"\tEnter the position of player {i + 1}: ")

                    # Create a new Player object with the provided name, position, and team
                    player = Player(player_name, player_position, team)

                    # Add the new player to the team's list of players
                    team.players.append(player)

            print(f"\n{num_of_players} players have been added to {
                  team.name}.")  # Print success message

            # Save the updated team data to a JSON file
            json.dump(self.teams_to_dict(self), open(
                '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

        except ValueError:
            # Handle case where user input is not an integer
            print("\nError: Please enter a valid number.")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"\nAn unexpected error occurred: {e}")

    def remove_players(self):
        try:
            # Prompt the user to select a team
            team = self.choose_team()

            # Check if the team has any players
            if len(team.players) == 0:
                print(f"\n{team.name} does not have any players.")
                return

            print()
            # Display all players in the team
            for i, player in enumerate(team.players, 1):
                print(f"\t{i}. {player.name}")

            # Keep asking for input until a valid number is entered
            while True:
                try:
                    # Prompt the user to enter the number of players to remove
                    num_of_players_to_remove = int(
                        input("\nHow many players would you like to remove: "))

                    # Validate the number of players to remove
                    if num_of_players_to_remove > len(team.players) or num_of_players_to_remove < 1:
                        print("\nInvalid number of players to remove.")
                    else:
                        break  # Exit the loop if the input is valid
                except ValueError:
                    print("\nError: Please enter a valid number.")

            # Remove the selected players from the team
            for _ in range(num_of_players_to_remove):
                player_to_remove = self.choose_player(team)
                team.players.remove(player_to_remove)
                print(f"\n{player_to_remove.name} has been removed from {
                      team.name}.")

            # Save the updated team data to a JSON file
            with open('2paradoteo\\codebace\\basketball_data.json', 'w') as file:
                json.dump(self.teams_to_dict(self), file, indent=4)

        except Exception as e:
            # Handle any other unexpected errors
            print(f"\nAn unexpected error occurred: {e}")
