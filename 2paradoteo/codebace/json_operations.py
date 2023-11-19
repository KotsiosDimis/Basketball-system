import json
import os

from player import Player
from team import Team

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
