import random
import time

class Team:
    def __init__(self, name, city, logo):
        self.name = name
        self.city = city
        self.logo = logo
        self.players = []
        self.wins = 0

class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

class BasketballLeague:
    def __init__(self, teams):
        self.teams = teams

    def create_team(self):
        name = input("\tEnter team name: ")
        city = input("\tEnter team city: ")
        logo = input("\tEnter team logo: ")
        team = Team(name, city, logo)
        self.teams.append(team)

    def create_player(self, team):
        name = input("Enter player name: ")
        position = input("Enter player position: ")
        team_name = team

        # Find the team with the given name
        team = next((t for t in self.teams if t.name == team_name), None)
        if team:
            player = Player(name, position, team)
            return player
        else:
            print(f"Team '{team_name}' not found.")
            return None

    def add_player_to_team(self, player):
        if player:
            player.team.players.append(player)

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
                print(f"\t{home_player.name} scores {home_points} points. Total score: {home_team_score} - {away_team_score}")
            
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

# Create an instance of the BasketballLeague class
league = BasketballLeague([])

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
        player = league.create_player(team.name)
        league.add_player_to_team(player)

# Start the championship
league.create_championship()
