class Team:
    def __init__(self, name, city, logo):
        # Initialize the Team object with the given name, city, and logo
        self.name = name
        self.city = city
        self.logo = logo

        # Create an empty list to store Player objects for the team
        self.players = []

        # Initialize the number of wins to 0
        self.wins = 0

    def team_to_dict(self):
        # Convert team information to a dictionary for JSON serialization
        return {
            "name": self.name,  # Add team name to the dictionary
            "city": self.city,  # Add team city to the dictionary
            "logo": self.logo,  # Add team logo to the dictionary
            # Add each player's dictionary representation to the list
            "players": [player.player_to_dict() for player in self.players],
            "wins": self.wins  # Add number of wins to the dictionary
        }
