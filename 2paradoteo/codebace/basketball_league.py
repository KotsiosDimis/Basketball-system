from team import Team
from player import Player
import json


class BasketballLeague:
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

    def simulate_match(self, home_team, away_team, points_to_win):
        # Initialize scores and ineligible players
        home_team_score = 0
        away_team_score = 0
        ineligible_players = set()

        # Print team names
        print(f"\n1. {home_team.name}\n")
        print(f"2. {away_team.name}\n")

        # Simulate a match between two teams until one team reaches a score of 2
        while home_team_score < points_to_win and away_team_score < points_to_win:

            # Loop for team selection
            while True:
                try:
                    # Prompt user to enter the number of the team that scored
                    scoring_team = input(
                        "\nEnter the number of the team that scored (1 or 2): ")

                    # Check if the input is valid
                    if scoring_team not in ('1', '2'):
                        raise ValueError(
                            "Invalid team number. Please enter 1 or 2.")

                    break  # Exit the loop if the input is valid
                except ValueError as e:
                    print(e)

            # Loop for action selection
            while True:
                try:
                    # Prompt user to select an action
                    print("\nMenu:\n")
                    print("\t1. Add Goal")
                    print("\t2. Add Assist")
                    print("\t3. Add Rebound")
                    print("\t4. Add Steal")
                    print("\t5. Add Block")
                    print("\t6. Add Foul")

                    action = input("\nSelect an action (1/2/3/4/5/6): ")

                    # Check if the input is valid
                    if action not in ('1', '2', '3', '4', '5', '6'):
                        raise ValueError(
                            "\nInvalid action. Please select a number from 1 to 6.")

                    break  # Exit the loop if the input is valid
                except ValueError as e:
                    print(e)

            # Update scores and player statistics based on the selected team and action
            if scoring_team == '1':
                home_player = self.choose_player(home_team, ineligible_players)

                if action == '1':
                    # If the action is to add a goal
                    home_points = self.get_points(
                        f"\nEnter the number of points for {home_player.name}'s shot: ")

                    # Update scores and Player's Goals for Team 1
                    home_team_score += home_points
                    home_player.points += home_points
                    print(f"\n\t{home_player.name} scores {home_points} points. Total score: {
                          home_team_score} - {away_team_score}")

                elif action == '2':
                    # If the action is to add an assist
                    home_player.assists += 1
                    print(f"\n\tAssist added! {home_player.name} has now {
                          home_player.assists} assists.")

                elif action == '3':
                    # If the action is to add a rebound
                    home_player.rebounds += 1
                    print(f"\n\tRebound added! {home_player.name} has now {
                          home_player.rebounds} rebounds.")

                elif action == '4':
                    # If the action is to add a steal
                    home_player.steals += 1
                    print(f"\n\tSteal added! {home_player.name} has now {
                          home_player.steals} steals.")

                elif action == '5':
                    # If the action is to add a block
                    home_player.blocks += 1
                    print(f"\n\tBlock added! {home_player.name} has now {
                          home_player.blocks} blocks.")

                elif action == '6':
                    # If the action is to add a foul
                    home_player.fouls += 1
                    print(f"\n\tFoul added! {home_player.name} has now {
                          home_player.fouls} fouls.")

                    # Check if the player has exceeded the foul limit
                    if home_player.fouls > 1:
                        ineligible_players.add(home_player)
                        print(
                            f"\n{home_player.name} has exceeded the foul limit and is now ineligible to continue playing.")

            elif scoring_team == '2':
                # If the scoring team is Team 2
                away_player = self.choose_player(away_team, ineligible_players)

                if action == '1':
                    # If the action is to add a goal
                    away_points = self.get_points(
                        f"\nEnter the number of points for {away_player.name}'s shot: ")

                    # Update scores and Player's Goals for Team 2
                    away_team_score += away_points
                    away_player.points += away_points
                    print(f"\n\t{away_player.name} scores {away_points} points. Total score: {
                          home_team_score} - {away_team_score}")

                elif action == '2':
                    # If the action is to add an assist
                    away_player.assists += 1
                    print(f"\n\tAssist added! {away_player.name} has now {
                          away_player.assists} assists.")

                elif action == '3':
                    # If the action is to add a rebound
                    away_player.rebounds += 1
                    print(f"\n\tRebound added! {away_player.name} has now {
                          away_player.rebounds} rebounds.")

                elif action == '4':
                    # If the action is to add a steal
                    away_player.steals += 1
                    print(f"\n\tSteal added! {away_player.name} has now {
                          away_player.steals} steals.")

                elif action == '5':
                    # If the action is to add a block
                    away_player.blocks += 1
                    print(f"\n\tBlock added! {away_player.name} has now {
                          away_player.blocks} blocks.")

                elif action == '6':
                    # If the action is to add a foul
                    away_player.fouls += 1
                    print(f"\n\tFoul added! {away_player.name} has now {
                          away_player.fouls} fouls.")

                    # Check if the player has exceeded the foul limit
                    if away_player.fouls > 1:
                        ineligible_players.add(away_player)
                        print(
                            f"\n{away_player.name} has exceeded the foul limit and is now ineligible to continue playing.")

            else:
                # If the scoring team input is not valid
                print("\nInvalid choice. Please try again.")

        return home_team_score, away_team_score

    def get_points(self, message):
        # Loop until a valid number of points is entered
        while True:
            try:
                # Prompt the user to enter a number of points
                points = int(input(message))
                # Check if the entered number of points is between 1 and 3
                if 1 <= points <= 3:
                    # Return the valid number of points
                    return points
                else:
                    # Print an error message if the entered number of points is not between 1 and 3
                    print(
                        "Invalid number of points. Please enter a number between 1 and 3.")
            except ValueError:
                # Print an error message if the entered value is not a number
                print("Invalid input. Please enter a number.")

    def create_championship(self):
        # Check if the number of teams is valid
        try:
            if len(self.teams) < 2:
                # Raise an exception if there are less than 2 teams
                raise ValueError(
                    "Number of teams must be greater than 1. Use the 'Append new Data' option to add more teams.")
            elif len(self.teams) % 2 != 0:
                # Raise an exception if the number of teams is not even
                raise ValueError("Number of teams must be even")

            # Ensure each team has more than 5 players
            for team in self.teams:
                if len(team.players) < 5:
                    # Raise an exception if a team has less than 5 players
                    raise ValueError(
                        f"Team {team.name} does not have enough players (minimum 5 required).")
        except ValueError as e:
            # Print the error message and exit the program
            print("\n" + str(e) + "\n")
            exit()

        while True:
            try:
                points_to_win = int(
                    input("\nEnter the number of points needed to win each match: "))
                if points_to_win > 0:  # Check if the input is a positive integer
                    break  # Exit the loop if the input is a valid integer
                else:
                    print("\nPlease enter a positive number.")
            except ValueError:
                # If the input is not a valid integer, print an error message and continue the loop
                print("\nInvalid input. Please enter a valid integer number.")
        # Generate the schedule of matches
        schedule = self.schedule_matches(self.teams)

        # Play the matches
        self.play_matches(schedule, points_to_win)

    def schedule_matches(self, teams):
        # Calculate the number of teams and rounds in the championship
        num_teams = len(teams)
        num_rounds = num_teams - 1

        # Calculate the number of matches per round
        matches_per_round = num_teams // 2

        # Initialize an empty schedule list to store the matches
        schedule = []

        # Iterate through each round
        for round in range(num_rounds):
            # Initialize an empty list to store the matches for the current round
            round_schedule = []

            # Iterate through each match in the round
            for match in range(matches_per_round):
                # Determine the home team and away team for the match
                home_team = teams[match]
                away_team = teams[num_rounds - match]

                # Add the match to the round_schedule list
                round_schedule.append((home_team, away_team))

            # Add the round_schedule list to the schedule list
            schedule.append(round_schedule)

            # Rotate the teams so that the next round has a different set of matches
            teams.insert(1, teams.pop())

        # Return the schedule of matches
        return schedule

    def play_matches(self, schedule, points_to_win):
        # Iterate over each round in the schedule
        for round, round_schedule in enumerate(schedule):
            # Print the round number
            print(f"\n\nRound {round + 1}\n")

            # Iterate over each match in the round schedule
            for match, (home_team, away_team) in enumerate(round_schedule):
                # Simulate the match and get the scores
                home_score, away_score = self.simulate_match(
                    home_team, away_team, points_to_win)

                # Update the wins for the home and away teams
                if home_score > away_score:
                    home_team.wins += 1
                else:
                    away_team.wins += 1

        # Print the final results
        print("\nThe Final Results are:\n")

        # Sort the teams based on the number of wins in descending order
        self.teams.sort(key=lambda x: x.wins, reverse=True)

        # Print the teams and their ranks
        for i, team in enumerate(self.teams, 1):
            print(f"{i} place: {team.name} - Wins: {team.wins}")

        # Save the teams data to a JSON file
        json.dump(self.teams_to_dict(self), open(
            '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

    def append_new_teams(self):
        try:
            # Get the current number of teams
            current_team_count = len(self.teams)

            # Check if the current total number of teams is even or odd
            if current_team_count % 2 == 0:
                # If even, prompt to add an even number of new teams
                print(f"Currently, there are {
                      current_team_count} teams, which is even. You need to add an even number of new teams to keep the total even.")
            else:
                # If odd, prompt to add an odd number of new teams
                print(f"Currently, there are {
                      current_team_count} teams, which is odd. You need to add an odd number of new teams to make the total even.")

            # Get the number of new teams to add from user input
            num_teams_to_add = int(
                input("Enter the number of new teams you want to add: "))

            # Validate that the total number of teams will be even after adding the new teams
            while (current_team_count + num_teams_to_add) % 2 != 0:
                if num_teams_to_add % 2 == 0:
                    # If the number of new teams is even, prompt to enter an odd number of new teams
                    print(
                        "You've entered an even number of new teams which would result in an odd total. Please enter an odd number of new teams.")
                else:
                    # If the number of new teams is odd, prompt to enter an even number of new teams
                    print(
                        "You've entered an odd number of new teams which would still result in an odd total. Please enter an even number of new teams.")
                num_teams_to_add = int(
                    input("Enter a different number of teams to add: "))

            # Get the index of the last existing team
            last_existing_team_index = len(self.teams)

            # Create the new teams
            self.create_teams(num_teams_to_add)

            # Get the number of players per team from user input
            while True:
                try:
                    num_players_per_team = int(
                        input("\nEnter the number of players per team (between 5 and 10): "))
                    if 5 <= num_players_per_team <= 10:
                        break
                    else:
                        print(
                            "Invalid range. Please enter a number between 5 and 10.")
                except ValueError:
                    print("\n\tInvalid input. Please enter a number.")

            # Validate the number of players per team
            while num_players_per_team < 5 or num_players_per_team > 10:
                print(
                    "\n\tInvalid number of players. Each team must have between 5 and 10 players.\n")
                num_players_per_team = int(
                    input("Please enter the number of players per team (between 5 and 10): "))

            # Create players for the new teams
            for i in range(last_existing_team_index, len(self.teams)):
                self.create_players_for_team(
                    self.teams[i], num_players_per_team)

            # Save the updated teams to a JSON file
            json.dump(self.teams_to_dict(self), open(
                '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")

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

    def show_total_team_statistics(self):
        # Prompt the user to choose a team
        team = self.choose_team()

        # Calculate the counters for the chosen team
        counters = self.counters(team)

        # Print the total team statistics for the chosen team
        print(f"\nTotal team statistics for {team.name}:")
        print(f"Points: {counters['total_points']}")
        print(f"Assists: {counters['total_assists']}")
        print(f"Rebounds: {counters['total_rebounds']}")
        print(f"Steals: {counters['total_steals']}")
        print(f"Blocks: {counters['total_blocks']}")
        print(f"Fouls: {counters['total_fouls']}")

    def calculate_averages(self):
        # Choose the team for which we want to calculate averages
        team = self.choose_team()

        # Count the number of occurrences of each stat for the team
        counters = self.counters(team)

        # Calculate the total number of players in the team
        total_players = len(team.players)

        # Print the header for the averages
        print(f"\nAverages for {team.name} Team:\n")

        # Iterate over each stat and calculate the average
        for stat in ["points", "rebounds", "assists", "steals", "blocks", "fouls"]:
            # Calculate the average for the current stat
            average = counters[f'total_{stat}'] / \
                total_players if total_players > 0 else 0

            # Print the average with the stat name capitalized and formatted to 2 decimal places
            print(f"\t{stat.capitalize()}: {average:.2f}")

    def counters(self, team):
        # Calculate the total points by summing up the points of each player in the team
        total_points = sum(player.points for player in team.players)

        # Calculate the total assists by summing up the assists of each player in the team
        total_assists = sum(player.assists for player in team.players)

        # Calculate the total rebounds by summing up the rebounds of each player in the team
        total_rebounds = sum(player.rebounds for player in team.players)

        # Calculate the total steals by summing up the steals of each player in the team
        total_steals = sum(player.steals for player in team.players)

        # Calculate the total blocks by summing up the blocks of each player in the team
        total_blocks = sum(player.blocks for player in team.players)

        # Calculate the total fouls by summing up the fouls of each player in the team
        total_fouls = sum(player.fouls for player in team.players)

        # Return a dictionary with the calculated totals
        return {
            'total_points': total_points,
            'total_assists': total_assists,
            'total_rebounds': total_rebounds,
            'total_steals': total_steals,
            'total_blocks': total_blocks,
            'total_fouls': total_fouls
        }

    def show_MVP(self):
        # Create a list of all players from all teams
        all_players = [
            player for team in self.teams for player in team.players]

        # Find the player with the maximum number of points
        mvp = max(all_players, key=lambda player: player.points)

        # Print the name and points of the MVP
        print(f"\n{mvp.name} is the MVP of the Tournament with {
              mvp.points} points.")

    def show_player_statistics(self):
        # Prompt the user to choose a team
        team = self.choose_team()

        # Prompt the user to choose a player from the selected team
        player = self.choose_player(team)

        # Convert the player object to a dictionary using the to_dict method
        player_stats = player.player_to_dict()

        # Print the statistics for the selected player in the selected team
        print(f"\nStatistics for {player.name} in {team.name} Team:\n")

        # Iterate over each stat and value in the player_stats dictionary
        for stat, value in player_stats.items():
            # Exclude the 'name' and 'position' stats from being printed
            if stat != 'name' and stat != 'position':
                # Print the capitalized stat name and its corresponding value
                print(f"\t{stat.capitalize()}: {value}")
