import json
import os


class Team:
    def __init__(self, name, city, logo):
        # Team constructor initializes attributes
        self.name = name
        self.city = city
        self.logo = logo
        self.players = []  # List to store Player objects for the team
        self.wins = 0


class Player:
    def __init__(self, name, position, team):
        # Player constructor initializes attributes
        self.name = name
        self.position = position
        self.team = team
        self.points = 0
        self.rebounds = 0
        self.assists = 0
        self.steals = 0
        self.blocks = 0
        self.fouls = 0


class BasketballLeague:
    def __init__(self, teams):
        # BasketballLeague constructor initializes teams attribute
        self.teams = teams

    def create_teams(self, num_teams):
        # Create teams with default names, cities, and logos
        for i in range(num_teams):
            team = Team(f"NTeam{i+1}", f"NCity{i+1}", f"NLogo{i+1}")
            self.teams.append(team)

    def create_players_for_team(self, team, num_players):
        # Create players for a given team
        for i in range(num_players):
            player = Player(f"Player{i+1}", f"Position{i+1}", team)
            team.players.append(player)

    def simulate_match(self, home_team, away_team):
        # Simulate a basketball match between two teams
        home_team_score = 0
        away_team_score = 0

        print(f"\n1. {home_team.name}\n")
        print(f"2. {away_team.name}\n")

        while home_team_score < 2 and away_team_score < 2:
            scoring_team = input("Enter the number of the team that scored  (1 or 2): ")

            if scoring_team == '1':
                home_player = self.choose_player(home_team)
                home_points = self.get_points("Enter the number of points for " + home_player.name + "'s shot: ")
                home_team_score += home_points
                home_player.points += home_points
                print(f"\t{home_player.name} scores {home_points} points. Total score: {home_team_score} - {away_team_score}")

            elif scoring_team == '2':
                away_player = self.choose_player(away_team)
                away_points = self.get_points("Enter the number of points for " + away_player.name + "'s shot: ")
                away_team_score += away_points
                away_player.points += away_points
                print(f"\t{away_player.name} scores {away_points} points. Total score: {home_team_score} - {away_team_score}")
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
                    print("Invalid number of points. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def choose_player(self, team):
        # Choose a player from a given team
        print(f"\nChoose a player from {team.name}:")
        for i, player in enumerate(team.players, 1):
            print(f"{i}. {player.name}")

        while True:
            try:
                choice = int(input("Enter the player number: "))
                if 1 <= choice <= len(team.players):
                    return team.players[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid player number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def create_championship(self):
        # Create a championship schedule and play matches
        if len(self.teams) % 2 != 0:
            raise ValueError("Number of teams must be even")

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
                home_score, away_score = self.simulate_match(home_team, away_team)

                if home_score > away_score:
                    home_team.wins += 1
                else:
                    away_team.wins += 1

        print("\nThe Final Results are:\n")
        self.teams.sort(key=lambda x: x.wins, reverse=True)
        for i, team in enumerate(self.teams, 1):
            print(f"{i} place: {team.name} - Wins: {team.wins}")


class JSONOperations:
    def __init__(self, filename):
        # JSONOperations constructor initializes the filename attribute
        self.filename = filename

    def teams_to_dict(self, league):
        # Convert league information to a dictionary for JSON serialization
        teams_dict = {"teams": []}
        for team in league.teams:
            team_dict = {
                "name": team.name,
                "city": team.city,
                "logo": team.logo,
                "players": [
                    {"name": player.name, "position": player.position, "points": player.points,
                     "rebounds": player.rebounds, "assists": player.assists, "steals": player.steals,
                     "blocks": player.blocks, "fouls": player.fouls} for player in team.players],
                "wins": team.wins
            }
            teams_dict["teams"].append(team_dict)
        return teams_dict

    def append_to_json_file(self, league):
        # Append league information to an existing JSON file
        with open(self.filename, 'r+') as f:
            file_data = json.load(f)
            file_data.update({"teams": self.teams_to_dict(league)["teams"]})
            f.seek(0)
            json.dump(file_data, f, indent=4)
            f.truncate()

    def handle_json(self):
        # Read and handle information from an existing JSON file
        with open(self.filename, "r") as file:
            data = json.load(file)

        teams = data["teams"]
        team_objects = []

        for team in teams:
            team_obj = Team(team["name"], team["city"], team["logo"])
            team_obj.wins = team["wins"]

            for player in team["players"]:
                player_obj = Player(player["name"], player["position"], team_obj)
                team_obj.players.append(player_obj)

            team_objects.append(team_obj)

        return team_objects

    def reset_numerical_values(self):
        # Reset numerical values (wins, points, rebounds, etc.) in the JSON file
        if os.path.exists(self.filename):
            with open(self.filename, 'r+') as f:
                file_data = json.load(f)

                for team in file_data['teams']:
                    team['wins'] = 0
                    for player in team['players']:
                        player['points'] = 0
                        player['rebounds'] = 0
                        player['assists'] = 0
                        player['steals'] = 0
                        player['blocks'] = 0
                        player['fouls'] = 0

                f.seek(0)
                json.dump(file_data, f, indent=4)
                f.truncate()

            print("Numerical values reset successfully.")
        else:
            print(f"Error: '{self.filename}' not found.")

    def delete_data(self):
        # Delete all data in the JSON file
        if os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write('')
            print("Data cleared successfully.")
        else:
            print(f"Error: '{self.filename}' not found.")


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
