from team import Team
from player import Player
import json


class BasketballLeague:
    def __init__(self, teams):
        # BasketballLeague constructor initializes teams attribute
        self.teams = teams

    def teams_to_dict(self, league):
        teams_dict = {"teams": []}
        for team in league.teams:
            teams_dict["teams"].append(team.team_to_dict())
        return teams_dict

    def create_teams(self, num_teams):
        # Create teams with custom names, cities, and logos
        for i in range(num_teams):
            team_name = input(f"Enter the name for Team {i+1}: ")
            city = input(f"Enter the city for Team {i+1}: ")
            logo = input(f"Enter the logo for Team {i+1}: ")
            team = Team(team_name, city, logo)
            self.teams.append(team)

    def create_players_for_team(self, team, num_players):
        # Create players for a given team with custom names and positions
        for i in range(num_players):
            player_name = input(f"Enter the name for Player {
                                i+1} in {team.name}: ")
            position = input(f"Enter the position for Player {
                             i+1} in {team.name}: ")
            player = Player(player_name, position, team)
            team.players.append(player)

    def simulate_match(self, home_team, away_team):
        # Simulate a basketball match between two teams
        home_team_score = 0
        away_team_score = 0
        ineligible_players = set()

        print(f"\n1. {home_team.name}\n")
        print(f"2. {away_team.name}\n")
        # TODO: Change the scoring to user's choice or bigger value
        # Simulate a match between two teams
        while home_team_score < 2 and away_team_score < 2:

            while True:  # Loop for team selection
                try:
                    scoring_team = input(
                        "Enter the number of the team that scored (1 or 2): ")
                    if scoring_team not in ('1', '2'):
                        raise ValueError(
                            "Invalid team number. Please enter 1 or 2.")
                    break  # Exit the loop if the input is valid
                except ValueError as e:
                    print(e)

            while True:  # Loop for action selection
                try:
                    print("Menu:")
                    print("1. Add Goal")
                    print("2. Add Assist")
                    print("3. Add Rebound")
                    print("4. Add Steal")
                    print("5. Add Block")
                    print("6. Add Foul")

                    action = input("Select an action (1/2/3/4/5/6): ")
                    if action not in ('1', '2', '3', '4', '5', '6'):
                        raise ValueError(
                            "Invalid action. Please select a number from 1 to 6.")
                    break  # Exit the loop if the input is valid
                except ValueError as e:
                    print(e)

            if scoring_team == '1':
                home_player = self.choose_player(home_team, ineligible_players)
                if action == '1':
                    home_points = self.get_points(
                        "Enter the number of points for " + home_player.name + "'s shot: ")
                    home_team_score += home_points
                    home_player.points += home_points
                    print(f"\t{home_player.name} scores {home_points} points. Total score: {
                          home_team_score} - {away_team_score}")
                elif action == '2':
                    home_player.assists += 1
                    print(f"\nAssist added! {home_player.name} has now {
                          home_player.assists} assists.")
                elif action == '3':
                    home_player.rebounds += 1
                    print(f"\nRebound added! {home_player.name} has now {
                          home_player.rebounds} rebounds.")
                elif action == '4':
                    home_player.steals += 1
                    print(f"\nSteal added! {home_player.name} has now {
                          home_player.steals} steals.")
                elif action == '5':
                    home_player.blocks += 1
                    print(f"Block added! {home_player.name} has now {
                          home_player.blocks} blocks.")
                elif action == '6':
                    home_player.fouls += 1
                    print(f"Foul added! {home_player.name} has now {
                          home_player.fouls} fouls.")
                    if home_player.fouls > 1:
                        ineligible_players.add(home_player)
                        print(
                            f"{home_player.name} has exceeded the foul limit and is now ineligible to continue playing.")

            elif scoring_team == '2':
                away_player = self.choose_player(away_team, ineligible_players)
                if action == '1':
                    away_points = self.get_points(
                        "Enter the number of points for " + away_player.name + "'s shot: ")
                    away_team_score += away_points
                    away_player.points += away_points
                    print(f"\t{away_player.name} scores {away_points} points. Total score: {
                          home_team_score} - {away_team_score}")
                elif action == '2':
                    away_player.assists += 1
                    print(f"Assist added! {away_player.name} has now {
                          away_player.assists} assists.")
                elif action == '3':
                    away_player.rebounds += 1
                    print(f"Rebound added! {away_player.name} has now {
                          away_player.rebounds} rebounds.")
                elif action == '4':
                    away_player.steals += 1
                    print(f"Steal added! {away_player.name} has now {
                          away_player.steals} steals.")
                elif action == '5':
                    away_player.blocks += 1
                    print(f"Block added! {away_player.name} has now {
                          away_player.blocks} blocks.")
                elif action == '6':
                    away_player.fouls += 1
                    print(f"Foul added! {away_player.name} has now {
                          away_player.fouls} fouls.")
                    if away_player.fouls > 1:
                        ineligible_players.add(away_player)
                        print(
                            f"{away_player.name} has exceeded the foul limit and is now ineligible to continue playing.")

            else:
                print("Invalid choice. Please try again.")

        return home_team_score, away_team_score

    def get_points(self, message):
        # Get the number of points for a shot, validated between 1 and 3
        while True:
            try:
                points = int(input(message))
                if 1 <= points <= 3:
                    return points
                else:
                    print(
                        "Invalid number of points. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def create_championship(self):
        # Create a championship schedule and play matches
        try:
            if len(self.teams) < 2:
                raise ValueError(
                    "Number of teams must be greater than 1. Use the 'Append new Data' option to add more teams.")
            elif len(self.teams) % 2 != 0:
                raise ValueError("Number of teams must be even")

            # Ensure each team has more than 5 players
            for team in self.teams:
                if len(team.players) < 5:
                    raise ValueError(
                        f"Team {team.name} does not have enough players (minimum 5 required).")

        except ValueError as e:
            print(e)
            exit()

        schedule = self.schedule_matches(self.teams)
        self.play_matches(schedule)

    def schedule_matches(self, teams):
        # Schedule matches for each round of the championship
        num_teams = len(teams)
        num_rounds = num_teams - 1
        matches_per_round = num_teams // 2

        schedule = []

        for round in range(num_rounds):
            round_schedule = []
            for match in range(matches_per_round):
                home_team = teams[match]
                away_team = teams[num_rounds - match]
                round_schedule.append((home_team, away_team))
            schedule.append(round_schedule)
            teams.insert(1, teams.pop())
        return schedule

    def play_matches(self, schedule):
        # Play matches and update team wins
        for round, round_schedule in enumerate(schedule):
            print(f"\n\nRound {round + 1}\n")

            for match, (home_team, away_team) in enumerate(round_schedule):
                home_score, away_score = self.simulate_match(
                    home_team, away_team)

                if home_score > away_score:
                    home_team.wins += 1
                else:
                    away_team.wins += 1

        print("\nThe Final Results are:\n")
        self.teams.sort(key=lambda x: x.wins, reverse=True)
        for i, team in enumerate(self.teams, 1):
            print(f"{i} place: {team.name} - Wins: {team.wins}")

        json.dump(self.teams_to_dict(self), open(
            '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

    def append_new_teams(self):
        current_team_count = len(self.teams)
        print(
            "To maintain a balanced championship, the total number of teams must be even.")
        if current_team_count % 2 == 0:
            print(f"Currently, there are {
                  current_team_count} teams, which is even. You need to add an even number of new teams to keep the total even.")
        else:
            print(f"Currently, there are {
                  current_team_count} teams, which is odd. You need to add an odd number of new teams to make the total even.")

        num_teams_to_add = int(
            input("Enter the number of new teams you want to add: "))
        while (current_team_count + num_teams_to_add) % 2 != 0:
            if num_teams_to_add % 2 == 0:
                print("You've entered an even number of new teams which would result in an odd total. Please enter an odd number of new teams.")
            else:
                print("You've entered an odd number of new teams which would still result in an odd total. Please enter an even number of new teams.")
            num_teams_to_add = int(
                input("Enter a different number of teams to add: "))
        last_existing_team_index = len(self.teams)
        self.create_teams(num_teams_to_add)

        num_players_per_team = int(
            input("\nEnter the number of players per team (between 5 and 10): "))

        while num_players_per_team < 5 or num_players_per_team > 10:
            print(
                "Invalid number of players. Each team must have between 5 and 10 players.")
            num_players_per_team = int(
                input("Please enter the number of players per team (between 5 and 10): "))

        for i in range(last_existing_team_index, len(self.teams)):
            self.create_players_for_team(self.teams[i], num_players_per_team)

        json.dump(self.teams_to_dict(self), open(
            '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

    def exchange_players(self):
        # Display teams and prompt user to choose two teams
        print("Choose two teams to exchange players between:")
        for i, team in enumerate(self.teams, 1):
            # Using dot notation to access the name attribute
            print(f"{i}. {team.name}")

        first_team_index = int(
            input("Enter the number for the first team: ")) - 1
        second_team_index = int(
            input("Enter the number for the second team: ")) - 1

        # Ensure the chosen teams are different
        if first_team_index == second_team_index:
            print("Please select two different teams.")
            return

        # Select player from the first team
        first_team = self.teams[first_team_index]
        print(f"\nChoose a player from {first_team.name}:")
        # Assuming players is a list attribute
        for i, player in enumerate(first_team.players, 1):
            # Adjust based on how a player is represented
            print(f"{i}. {player.name}")
        first_player_index = int(input("Enter the player number: ")) - 1

        # Select player from the second team
        second_team = self.teams[second_team_index]
        print(f"\nChoose a player from {second_team.name}:")
        for i, player in enumerate(second_team.players, 1):
            print(f"{i}. {player.name}")
        second_player_index = int(input("Enter the player number: ")) - 1

        # Exchange the players
        first_team.players[first_player_index], second_team.players[second_player_index] = \
            second_team.players[second_player_index], first_team.players[first_player_index]

        print(f"Exchanged players between {
              first_team.name} and {second_team.name}.")

        json.dump(self.teams_to_dict(self), open(
            '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

    def add_new_players(self):
        # Add a new player to a team
        team = self.choose_team()
        if len(team.players) >= 10:
            print(f"{team.name} already has the maximum number of players.")
            return
        print(f"There are currently {
              len(team.players)} players in the team and the maximum is 10.")
        numofplayers = int(input("Enter the number of players to add: "))
        if len(team.players) + numofplayers > 10:
            print(f"{team.name} reached {len(team.players) +
                  numofplayers} players, which is more than the maximum of 10.")
            return
        else:
            for i in range(numofplayers):
                player_name = input(f"Enter the name of player {i+1}: ")
                player_position = input(
                    f"Enter the position of player {i+1}: ")
                player = Player(player_name, player_position, team)
                team.players.append(player)
        print(f"{numofplayers} players have been added to {team.name}.")

        json.dump(self.teams_to_dict(self), open(
            '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

    def remove_players(self):
        # Remove players from a team
        team = self.choose_team()
        if len(team.players) == 0:
            print(f"{team.name} does not have any players.")
            return

        # Display all players in the team
        for i, player in enumerate(team.players, 1):
            print(f"{i}. {player.name}")

        # Get the number of players to remove and validate it
        num_of_players_to_remove = int(
            input("How many players would you like to remove: "))
        if num_of_players_to_remove > len(team.players) or num_of_players_to_remove < 1:
            print("Invalid number of players to remove.")
            return

        # Remove the selected players from the team
        for _ in range(num_of_players_to_remove):
            player_to_remove = self.choose_player(team)
            team.players.remove(player_to_remove)
            print(f"{player_to_remove.name} has been removed from {team.name}.")

        json.dump(self.teams_to_dict(self), open(
            '2paradoteo\\codebace\\basketball_data.json', 'w'), indent=4)

    def choose_player(self, team, ineligible_players=None):
        if ineligible_players is None:
            ineligible_players = set()

        # Filter out ineligible players and players with 3 or more fouls
        eligible_players = [
            player for player in team.players if player not in ineligible_players]
        print(f"\nChoose a player from {team.name}:")

        for i, player in enumerate(eligible_players, 1):
            print(f"{i}. {player.name}")

        while True:
            try:
                player_number = int(input("Enter the number of the player: "))
                if 1 <= player_number <= len(eligible_players):
                    return eligible_players[player_number - 1]
                else:
                    print("Invalid player number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def choose_team(self):
        # Choose a team
        print("\nChoose a team:")
        for i, team in enumerate(self.teams, 1):
            print(f"{i}. {team.name}")

        while True:
            try:
                team_index = int(input("Enter the team number: ")) - 1
                if 0 <= team_index < len(self.teams):
                    return self.teams[team_index]
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {
                          len(self.teams)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def show_total_team_statistics(self):
        team = self.choose_team()
        counters = self.counters(team)

        print(f"\nTotal team statistics for {team.name}:")
        print(f"Points: {counters['total_points']}")
        print(f"Assists: {counters['total_assists']}")
        print(f"Rebounds: {counters['total_rebounds']}")
        print(f"Steals: {counters['total_steals']}")
        print(f"Blocks: {counters['total_blocks']}")
        print(f"Fouls: {counters['total_fouls']}")

    def calculate_averages(self):
        team = self.choose_team()
        counters = self.counters(team)
        total_players = len(team.players)

        print(f"\nAverages for {team.name} Team:")
        for stat in ["points", "rebounds", "assists", "steals", "blocks", "fouls"]:
            average = counters[f'total_{stat}'] / \
                total_players if total_players > 0 else 0
            # Format for 2 decimal places
            print(f"{stat.capitalize()}: {average:.2f}")

    def counters(self, team):
        total_points = sum(player.points for player in team.players)
        total_assists = sum(player.assists for player in team.players)
        total_rebounds = sum(player.rebounds for player in team.players)
        total_steals = sum(player.steals for player in team.players)
        total_blocks = sum(player.blocks for player in team.players)
        total_fouls = sum(player.fouls for player in team.players)

        return {
            'total_points': total_points,
            'total_assists': total_assists,
            'total_rebounds': total_rebounds,
            'total_steals': total_steals,
            'total_blocks': total_blocks,
            'total_fouls': total_fouls
        }

    def show_MVP(self):
        all_players = [
            player for team in self.teams for player in team.players]
        mvp = max(all_players, key=lambda player: player.points)
        print(f"\n{mvp.name} is the MVP of the Tournament with {
              mvp.points} points.")

    def show_player_statistics(self):
        team = self.choose_team()
        player = self.choose_player(team)

        # Using to_dict method from Player class
        player_stats = player.player_to_dict()
        print(f"\nStatistics for {player.name} in {team.name} Team:")
        for stat, value in player_stats.items():
            if stat != 'name' and stat != 'position':  # Assuming you don't want to print name and position here
                print(f"{stat.capitalize()}: {value}")
