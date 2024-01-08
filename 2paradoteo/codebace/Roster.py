from Team import Team
from Player import Player


class Roster:
    def __init__(self, teams):
        # Initialize the teams attribute with the provided teams parameter.
        self.teams = teams

    def teams_to_dict(self, league):
        # Initialize an empty dictionary to store the teams
        teams_dict = {"teams": []}

        # Iterate through each team in the league
        for team in league.teams:
            # Convert each team to a dictionary using the team_to_dict() method
            team_dict = team.team_to_dict()

            # Append the team dictionary to the list of teams in the teams_dict
            teams_dict["teams"].append(team_dict)

        # Return the dictionary containing all the teams
        return teams_dict

    def create_teams(self, num_teams):

        # Iterate over the range of num_teams
        for i in range(num_teams):

            # Prompt the user for the team name, city, and logo
            team_name = input(f"Enter the name for Team {i+1}: ")
            city = input(f"Enter the city for Team {i+1}: ")
            logo = input(f"Enter the logo for Team {i+1}: ")

            # Create a new Team object with the provided information
            team = Team(team_name, city, logo)

            # Add the team to the list of teams
            self.teams.append(team)

    def create_players_for_team(self, team, num_players):
        # Iterate over the range of num_players
        for i in range(num_players):
            # Prompt the user to enter the name for the current player in the given team
            player_name = input(f"Enter the name for Player {
                                i+1} in {team.name}: ")
            # Prompt the user to enter the position for the current player in the given team
            position = input(f"Enter the position for Player {
                             i+1} in {team.name}: ")

            # Create a new Player object with the entered name, position, and team
            player = Player(player_name, position, team)

            # Add the created player to the list of players in the team
            team.players.append(player)

    def choose_player(self, team, ineligible_players=None):
        # If ineligible_players is not provided, set it to an empty set
        if ineligible_players is None:
            ineligible_players = set()

        # Create a list of eligible players by filtering out ineligible players
        eligible_players = [
            player for player in team.players if player not in ineligible_players]

        # Print a message to prompt the user to choose a player from the given team
        print(f"\nChoose a player from {team.name}:\n")

        # Print the list of eligible players with their corresponding numbers
        for i, player in enumerate(eligible_players, 1):
            print(f"\t{i}. {player.name}")

        # Keep asking the user for input until a valid player number is entered
        while True:
            try:
                # Prompt the user to enter the number of the player
                player_number = int(
                    input("\nEnter the number of the player: "))

                # Check if the entered player number is within the valid range
                if 1 <= player_number <= len(eligible_players):
                    # Return the selected player
                    return eligible_players[player_number - 1]
                else:
                    # Print an error message for invalid player number
                    print("\nInvalid player number. Please try again.")
            except ValueError:
                # Print an error message for invalid input (not a number)
                print("\nInvalid input. Please enter a number.")

    def choose_team(self, selected_team=None):
        # If selected_team is not provided or None, initialize it as an empty set
        if selected_team is None:
            selected_team = set()

        print("\nChoose a team:\n")

        # Filter out already selected teams and display the remaining ones
        available_teams = [
            team for team in self.teams if team.name not in selected_team]
        for i, team in enumerate(available_teams, 1):
            print(f"\t{i}. {team.name}")

        # Keep asking for input until a valid team number is entered
        while True:
            try:
                team_number = int(input("\nEnter the team number: "))
                team_index = team_number - 1

                # Check if the entered team number corresponds to an available team
                if 0 <= team_index < len(available_teams):
                    chosen_team = available_teams[team_index]
                    # Add the chosen team to the set of selected teams
                    selected_team.add(chosen_team.name)
                    return chosen_team
                else:
                    if (len(available_teams) == 1):
                        print("\nThere is only one team available. Please choose it.")
                    else:
                        print(f"\nInvalid choice. Please enter a number between 1 and {
                            len(available_teams)}.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
