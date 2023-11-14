import json
import os

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = [Player(player_data["playerName"], player_data["position"], self) for player_data in players]
        self.wins = 0

class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

class BasketballLeague:
    def __init__(self, teams):
        self.teams = [Team(team_data["teamName"], team_data["players"]) for team_data in teams]

    def create_team(self):
        name = input("\tEnter team name: ")
        team = Team(name, [])
        self.teams.append(team)

    def create_player(self, team):
        name = input("Enter player name: ")
        position = input("Enter player position: ")
        player = Player(name, position, team)
        return player

    def add_player_to_team(self, team, player):
        team.players.append(player)

    def simulate_match(self, home_team, away_team):
        home_team_score = 0
        away_team_score = 0
    
        print(f"\n1. {home_team.name}\n")
        print(f"2. {away_team.name}\n")
        
        while home_team_score < 22 and away_team_score < 22:
            scoring_team = input("Enter the number of the team that scored  (1 or 2): ")
    
            if scoring_team == '1':
                home_player = self.choose_player(home_team)
                home_points = self.get_points("Enter the number of points for " + home_player.name + "'s shot: ")
                home_team_score += home_points
                print(f"\t{home_player.name} scores {home_points} points. Total score: {home_team_score} - {away_team_score}\n")
            
            elif scoring_team == '2':
                away_player = self.choose_player(away_team)
                away_points = self.get_points("Enter the number of points for " + away_player.name + "'s shot: ")
                away_team_score += away_points
                print(f"\t{away_player.name} scores {away_points} points. Total score: {home_team_score} - {away_team_score}")
            else:
                print("Invalid choice. Please try again.")
            
    
        return home_team_score, away_team_score
            

    def get_points(self, message):
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
        if len(self.teams) % 2 != 0:
            raise ValueError("Number of teams must be even")

        schedule = self.schedule_matches(self.teams)
        self.play_matches(schedule)

    def schedule_matches(self, teams):
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

    def save_to_json(self, filename='basketball_data.json'):
        data = []
        for team in self.teams:
            team_data = {"teamName": team.name, "players": []}
            for player in team.players:
                player_data = {"playerName": player.name, "position": player.position}
                team_data["players"].append(player_data)
            data.append(team_data)

        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

# Prompt the user for the data loading option
while True:
    print("\nChoose an option:")
    print("1. Use existing data")
    print("2. Append new data")
    print("3. Delete all existing data and start fresh")
    option = input("Enter the option number (1/2/3): ")

    if option == '1':
        if os.path.exists('basketball_data.json'):
            with open('basketball_data.json') as json_file:
                data = json.load(json_file)
            league = BasketballLeague(data)
            break
        else:
            print("Error: 'basketball_data.json' not found. Please choose option 2 or 3.")
    elif option == '2':
        league = BasketballLeague([])
        break
    elif option == '3':
        league = BasketballLeague([])
        break
    else:
        print("Invalid option. Please enter 1, 2, or 3.")

# If the user chose option 2 or 3, allow them to create teams and players
if option in ['2', '3']:
    # User creates teams
    num_teams = int(input("Enter the number of teams for the league: "))
    for i in range(num_teams):
        print("\n Create Team " + str(i + 1) + "\n")
        league.create_team()

    # User creates players for each team
    num_players_per_team = int(input("\n  Enter the number of players per team: "))
    for team in league.teams:
        for i in range(num_players_per_team):
            print(f"\n Create " + str(i + 1) + " Player for Team " + team.name +"\n")
            player = league.create_player(team)
            league.add_player_to_team(team, player)

    # Save the data to the JSON file
    league.save_to_json()

# Start the championship
league.create_championship()
