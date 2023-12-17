# team.py
class Team:
    def __init__(self, name, city, logo):
        # Team constructor initializes attributes
        self.name = name
        self.city = city
        self.logo = logo
        self.players = []  # List to store Player objects for the team
        self.wins = 0

    def team_to_dict(self):
        # Convert team information to a dictionary for JSON serialization
        return {
            "name": self.name,
            "city": self.city,
            "logo": self.logo,
            "players": [player.player_to_dict() for player in self.players],
            "wins": self.wins
        }
