import json
import os

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
        self.points = 0
        self.rebounds = 0
        self.assists = 0
        self.steals = 0
        self.blocks = 0
        self.fouls = 0


class BasketballLeague:
    def __init__(self, teams):
        self.teams = teams

    def create_teams(self, num_teams):
        for i in range(num_teams):
            team = Team(f"NTeam{i+1}", f"NCity{i+1}", f"NLogo{i+1}")
            self.teams.append(team)


    def create_players_for_team(self, team, num_players):
        for i in range(num_players):
            player = Player(f"Player{i+1}", f"Position{i+1}", team)
            team.players.append(player)

    def teams_to_dict(self):
        teams_dict = {"teams": []}
        for team in self.teams:
            team_dict = {
                "name": team.name,
                "city": team.city,
                "logo": team.logo,
                "players": [{"name": player.name, "position": player.position, "points": player.points, "rebounds": player.rebounds, "assists": player.assists, "steals": player.steals, "blocks": player.blocks, "fouls": player.fouls} for player in team.players],
                "wins": team.wins
            }
            teams_dict["teams"].append(team_dict)
        return teams_dict

    def append_to_json_file(self, filename = "2paradoteo\\codebace\\basketball_data.json"):
        with open(filename, 'r+') as f:
            file_data = json.load(f)
            file_data["teams"].extend(self.teams_to_dict()["teams"])
            f.seek(0)
            json.dump(file_data, f, indent=4)
    def add_player_to_team(self, player):
        if player:
            player.team.players.append(player)

    def simulate_match(self, home_team, away_team):
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

    def handle_json(self, json_data="2paradoteo\\codebace\\basketball_data.json"):
        # Load the JSON data from the provided file path
        with open(json_data, "r") as file:
            data = json.load(file)

        # Extract the "teams" list from the loaded JSON data
        teams = data["teams"]

        # Create an empty list to store the team objects
        team_objects = []

        # Iterate over each team in the "teams" list
        for team in teams:
            # Create a Team object with the name, city, and logo from the JSON data
            team_obj = Team(team["name"], team["city"], team["logo"])

            # Set the number of wins for the team
            team_obj.wins = team["wins"]

            # Iterate over each player in the "players" list of the current team
            for player in team["players"]:
                # Create a Player object with the name, position, and team object
                player_obj = Player(player["name"], player["position"], team_obj)

                # Add the player object to the players list of the team object
                team_obj.players.append(player_obj)

            # Add the team object to the list of team objects
            team_objects.append(team_obj)

        # Return the list of team objects
        return team_objects
    
    def delete_data(self, filename='2paradoteo\\codebace\\basketball_data.json'):
        if os.path.exists(filename):
            with open(filename, 'w'): pass
            print("Data cleared successfully.")
        else:
            print(f"Error: '{filename}' not found.")


while True:
    print("\nChoose an option:")
    print("1. Use existing data")
    print("2. Append new data")
    print("3. Delete all existing data and start fresh")
    print("4.Exit")
    option = input("Enter the option number (1/2/3): ")

    league = BasketballLeague([])

    if option == "1":
      if os.path.exists('2paradoteo\\codebace\\basketball_data.json'):  
        existing_teams=league.handle_json()
        league.teams.extend(existing_teams) 
        break
      else:
        print("Error: 'basketball_data.json' not found. Please choose option 2 or 3.")
    elif option == "2":
        num_teams = int(input("Enter the number of teams that you want to add: "))
        
        
        league.create_teams(num_teams)


        num_players_per_team = int(input("\n  Enter the number of players per team: "))
        for team in league.teams:
            league.create_players_for_team(team, num_players_per_team)

        existing_teams=league.handle_json()
        league.teams.extend(existing_teams)

        # Append teams to JSON file
        league.append_to_json_file('2paradoteo\\codebace\\basketball_data.json')
        break
    elif option == "3":
        league.delete_data()
        exit()
    elif option == "4":
        exit()
    else:
        print("Invalid option. Please enter 1, 2, or 3.")



# Start the championship
league.create_championship()


# # Create an instance of the BasketballLeague class
# league = BasketballLeague([])

# # User creates teams
# num_teams = int(input("Enter the number of teams for the league: "))
# for i in range(num_teams):
#     print("\n Create Team " + str(i + 1) + "\n")
#     league.create_team()

# # User creates players for each team
# num_players_per_team = int(input("\n  Enter the number of players per team: "))
# for team in league.teams:
#     for i in range(num_players_per_team):
#         print(f"\n Create " + str(i + 1) + " Player for Team " + team.name +"\n")
#         player = league.create_player(team.name)
#         league.add_player_to_team(player)