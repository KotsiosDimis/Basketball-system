import random
import time

# Define a Team class
class Team:
    def __init__(self, name, city, logo):
        self.name = name
        self.city = city
        self.logo = logo
        self.players = []  # List to store players in the team
        self.wins = 0  # Counter for team wins

# Define a Player class
class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

# Define a BasketballLeague class
class BasketballLeague:
    def __init__(self, teams):
        self.teams = teams  # List to store teams in the league

    # Method to create a new team and add it to the league
    def create_team(self, name, city, logo):
        team = Team(name, city, logo)
        self.teams.append(team)
        return team

    # Method to create a new player
    def create_player(self, name, position, team):
        player = Player(name, position, team)
        return player

    # Method to add a player to a team
    def add_player_to_team(self, player, team):
        player.team = team
        team.players.append(player)

    # Method to create a championship and schedule matches
    def create_championship(self, teams):
        if len(teams) % 2 != 0:
            raise ValueError("Number of teams must be even")

        schedule = self.schedule_matches(teams)
        self.play_matches(schedule)

    # Method to generate the schedule for matches
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

    # Method to simulate and play the matches
    def play_matches(self, schedule):
        for round, round_schedule in enumerate(schedule):
            print(f"\n\nRound {round + 1}\n")

            for match, (home_team, away_team) in enumerate(round_schedule):
                print(f"\n Match {match + 1}: {home_team.name} vs {away_team.name}\n")

                home_team_score = 0
                away_team_score = 0

                while home_team_score < 22 and away_team_score < 22:
                    if random.randint(0, 1) == 0:
                        home_player = home_team.players[random.randint(0, len(home_team.players) - 1)]
                        points = random.randint(1, 3)
                        home_team_score += points
                        print("\t" + home_player.name + " scores " + str(points) + " points.   Total score: " + str(
                            home_team_score) + " - " + str(away_team_score))
                        time.sleep(1)
                    else:
                        away_player = away_team.players[random.randint(0, len(away_team.players) - 1)]
                        points = random.randint(1, 3)
                        away_team_score += points
                        print("\t" + away_player.name + " scores " + str(points) + " points.   Total score: " + str(
                            home_team_score) + " - " + str(away_team_score))
                        time.sleep(1)

                if home_team_score > away_team_score:
                    home_team.wins += 1
                else:
                    away_team.wins += 1

        print(f"Result: {home_team_score} - {away_team_score}")
        print("\n The Final Results are : \n")
        teams.sort(key=lambda x: x.wins, reverse=True)
        print(f"1st place: {teams[0].name}")
        print(f"2nd place: {teams[1].name}")
        print(f"3rd place: {teams[2].name}")

# Create an instance of the BasketballLeague class
league = BasketballLeague([])

# Create teams
team1 = league.create_team("Golden State Warriors", "San Francisco", "Warriors_logo.png")
team2 = league.create_team("Boston Celtics", "Boston", "Celtics_logo.png")
team3 = league.create_team("Toronto Raptors", "Toronto", "Raptors_logo.png")
team4 = league.create_team("Milwaukee Bucks", "Milwaukee", "Bucks_logo.png")

# Create players for each team
player1 = league.create_player("Stephen Curry", "PG", team1)
player2 = league.create_player("Klay Thompson", "SG", team1)
player3 = league.create_player("Draymond Green", "SF", team1)
player4 = league.create_player("Andrew Wiggins", "PF", team1)
player5 = league.create_player("Jordan Poole", "C", team1)

player6 = league.create_player("Jayson Tatum", "PG", team2)
player7 = league.create_player("Jaylen Brown", "SG", team2)
player8 = league.create_player("Marcus Smart", "SF", team2)
player9 = league.create_player("Al Horford", "PF", team2)
player10 = league.create_player("Robert Williams III", "C", team2)

player11 = league.create_player("Scottie Barnes", "PG", team3)
player12 = league.create_player("Gary Trent Jr.", "SG", team3)
player13 = league.create_player("Pascal Siakam", "SF", team3)
player14 = league.create_player("OG Anunoby", "PF", team3)
player15 = league.create_player("Precious Achiuwa", "C", team3)

player16 = league.create_player("Giannis Antetokounmpo", "PG", team4)
player17 = league.create_player("Jrue Holiday", "SG", team4)
player18 = league.create_player("Khris Middleton", "SF", team4)
player19 = league.create_player("Bobby Portis Jr.", "PF", team4)
player20 = league.create_player("Brook Lopez", "C", team4)

# Add players to their respective teams
team1.players.extend([player1, player2, player3, player4, player5])
team2.players.extend([player6, player7, player8, player9, player10])
team3.players.extend([player11, player12, player13, player14, player15])
team4.players.extend([player16, player17, player18, player19, player20])

# Define a list of teams
teams = [team1, team2, team3, team4]

# Start the championship
league.create_championship(teams)
