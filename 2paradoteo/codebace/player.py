# player.py
class Player:
    def __init__(self, name, position, team):
        # Player constructor initializes attributes
        self.name = name
        self.position = position
        self.team = team
        self.points = 0
        # TODO: Implement counters for rebounds, assists, steals, blocks, and fouls
        # Ensure these counters are updated throughout the game.
        self.rebounds = 0
        self.assists = 0
        self.steals = 0
        self.blocks = 0
        self.fouls = 0


    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "points": self.points,
            "rebounds": self.rebounds,
            "assists": self.assists,
            "steals": self.steals,
            "blocks": self.blocks,
            "fouls": self.fouls
        }