import json
import os

from player import Player
from team import Team


class JSONOperations:
    def __init__(self, filename):
        # Initialize the filename attribute with the provided filename
        self.filename = filename

    def teams_to_dict(self, league):
        # Create an empty dictionary to store the teams information
        teams_dict = {"teams": []}

        # Iterate over each team in the league
        for team in league.teams:
            # Create a dictionary to store the information of each team
            team_dict = {
                "name": team.name,     # Store the name of the team
                "city": team.city,     # Store the city of the team
                "logo": team.logo,     # Store the logo of the team
                "players": [           # Create a list to store the information of each player in the team
                    player.player_to_dict() for player in team.players
                ],
                "wins": team.wins      # Store the number of wins of the team
            }
            # Append the team dictionary to the list of teams in the main dictionary
            teams_dict["teams"].append(team_dict)

        # Return the dictionary containing the teams information
        return teams_dict

    def handle_json(self):
        # Check if the file exists
        if not os.path.exists(self.filename):
            return []

        # Check if the file is empty
        if os.stat(self.filename).st_size == 0:
            return []

        # Open the file and load the JSON data
        with open(self.filename, "r") as file:
            data = json.load(file)

        # Extract the "teams" data from the JSON
        teams = data["teams"]
        team_objects = []

        # Iterate over each team in the "teams" data
        for team in teams:
            # Create a Team object with data from the JSON
            team_obj = Team(team["name"], team["city"], team["logo"])
            team_obj.wins = team["wins"]

            # Iterate over each player in the team data
            for player in team["players"]:
                # Create a Player object with data from the JSON
                player_obj = Player(
                    name=player["name"],
                    position=player["position"],
                    team=team_obj
                )

                # Assign values to player attributes, using .get() to provide defaults if not found
                player_obj.points = player.get("points", 0)
                player_obj.assists = player.get("assists", 0)
                player_obj.rebounds = player.get("rebounds", 0)
                player_obj.steals = player.get("steals", 0)
                player_obj.blocks = player.get("blocks", 0)
                player_obj.fouls = player.get("fouls", 0)

                # Add the player object to the team's list of players
                team_obj.players.append(player_obj)

            # Add the team object to the list of team objects
            team_objects.append(team_obj)

        # Return the list of team objects
        return team_objects

    def reset_numerical_values(self):
        # Check if the JSON file exists
        if os.path.exists(self.filename):
            # Open the file in read/write mode
            with open(self.filename, 'r+') as f:
                # Load the JSON data from the file
                file_data = json.load(f)

                # Iterate through each team in the JSON data
                for team in file_data['teams']:
                    # Reset the 'wins' value of the team to 0
                    team['wins'] = 0

                    # Iterate through each player in the team
                    for player in team['players']:
                        # Reset the numerical values (points, rebounds, assists, steals, blocks, fouls) of the player to 0
                        player['points'] = 0
                        player['rebounds'] = 0
                        player['assists'] = 0
                        player['steals'] = 0
                        player['blocks'] = 0
                        player['fouls'] = 0

                # Move the file pointer to the beginning of the file
                f.seek(0)

                # Write the modified JSON data back to the file with proper indentation
                json.dump(file_data, f, indent=4)

                # Truncate any remaining content in the file
                f.truncate()

            # Print success message
            print("Numerical values reset successfully.")
        else:
            # Print error message if the file is not found
            print(f"Error: '{self.filename}' not found.")

    def delete_data(self):
        # Check if the JSON file exists
        if os.path.exists(self.filename):
            # Open the JSON file in write mode
            with open(self.filename, 'w') as file:
                # Clear the contents of the file by writing an empty string
                file.write('')

            # Print a success message
            print("Data cleared successfully.")
        else:
            # Print an error message if the file is not found
            print(f"Error: '{self.filename}' not found.")
