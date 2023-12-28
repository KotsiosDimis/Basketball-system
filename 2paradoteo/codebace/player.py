
class Player:
    def __init__(self, name, position, team):
        # Initialize player attributes
        self.name = name  # Store player name
        self.position = position  # Store player position
        self.team = team  # Store player team
        self.points = 0  # Initialize player points
        self.rebounds = 0  # Initialize player rebounds
        self.assists = 0  # Initialize player assists
        self.steals = 0  # Initialize player steals
        self.blocks = 0  # Initialize player blocks
        self.fouls = 0  # Initialize player fouls

    def player_to_dict(self):
        # Return a dictionary representation of the player object
        return {
            "name": self.name,  # Add the player's name to the dictionary
            "position": self.position,  # Add the player's position to the dictionary
            "points": self.points,  # Add the player's points to the dictionary
            "rebounds": self.rebounds,  # Add the player's rebounds to the dictionary
            "assists": self.assists,  # Add the player's assists to the dictionary
            "steals": self.steals,  # Add the player's steals to the dictionary
            "blocks": self.blocks,  # Add the player's blocks to the dictionary
            "fouls": self.fouls  # Add the player's fouls to the dictionary
        }
