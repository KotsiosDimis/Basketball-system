from team import Team
from player import Player

class BasketballLeague:
    def __init__(self, teams):
        # BasketballLeague constructor initializes teams attribute
        self.teams = teams

    def create_teams(self, num_teams):
        # TODO: Change the creation of teams to custom names, cities, and logos
        # Create teams with default names, cities, and logos
        for i in range(num_teams):
            team = Team(f"NTeam{i+1}", f"NCity{i+1}", f"NLogo{i+1}")
            self.teams.append(team)

    def create_players_for_team(self, team, num_players):
        # TODO: Change the creation of players to custom names, positions, and teams
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
        # TODO: Change the scoring to user's choice or bigger value
        # Simulate a match between two teams
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