from Roster import Roster
import json


class Schedule(Roster):

    def __init__(self, teams):
        super().__init__(teams)

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
