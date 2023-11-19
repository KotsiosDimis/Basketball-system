# team.py
class Team:
    def __init__(self, name, city, logo):
        # Team constructor initializes attributes
        self.name = name
        self.city = city
        self.logo = logo
        self.players = []  # List to store Player objects for the team
        self.wins = 0
