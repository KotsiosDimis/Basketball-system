from Roster import Roster


class Stats(Roster):

    def __init__(self, teams):
        super().__init__(teams)

    def show_total_team_statistics(self):
        # Prompt the user to choose a team
        team = self.choose_team()

        # Calculate the counters for the chosen team
        counters = self.counters(team)

        # Print the total team statistics for the chosen team
        print(f"\nTotal team statistics for {team.name}:")
        print(f"\n\tPoints: {counters['total_points']}")
        print(f"\tAssists: {counters['total_assists']}")
        print(f"\tRebounds: {counters['total_rebounds']}")
        print(f"\tSteals: {counters['total_steals']}")
        print(f"\tBlocks: {counters['total_blocks']}")
        print(f"\tFouls: {counters['total_fouls']}")

    def calculate_averages(self):
        # Choose the team for which we want to calculate averages
        team = self.choose_team()

        # Count the number of occurrences of each stat for the team
        counters = self.counters(team)

        # Calculate the total number of players in the team
        total_players = len(team.players)

        # Print the header for the averages
        print(f"\nAverages for {team.name} Team:\n")

        # Iterate over each stat and calculate the average
        for stat in ["points", "rebounds", "assists", "steals", "blocks", "fouls"]:
            # Calculate the average for the current stat
            average = counters[f'total_{stat}'] / \
                total_players if total_players > 0 else 0

            # Print the average with the stat name capitalized and formatted to 2 decimal places
            print(f"\t{stat.capitalize()}: {average:.2f}")

    def counters(self, team):
        # Calculate the total points by summing up the points of each player in the team
        total_points = sum(player.points for player in team.players)

        # Calculate the total assists by summing up the assists of each player in the team
        total_assists = sum(player.assists for player in team.players)

        # Calculate the total rebounds by summing up the rebounds of each player in the team
        total_rebounds = sum(player.rebounds for player in team.players)

        # Calculate the total steals by summing up the steals of each player in the team
        total_steals = sum(player.steals for player in team.players)

        # Calculate the total blocks by summing up the blocks of each player in the team
        total_blocks = sum(player.blocks for player in team.players)

        # Calculate the total fouls by summing up the fouls of each player in the team
        total_fouls = sum(player.fouls for player in team.players)

        # Return a dictionary with the calculated totals
        return {
            'total_points': total_points,
            'total_assists': total_assists,
            'total_rebounds': total_rebounds,
            'total_steals': total_steals,
            'total_blocks': total_blocks,
            'total_fouls': total_fouls
        }

    def show_MVP(self):
        # Create a list of all players from all teams
        all_players = [
            player for team in self.teams for player in team.players]

        # Find the player with the maximum number of points
        mvp = max(all_players, key=lambda player: player.points)

        # Print the name and points of the MVP
        print(f"\n{mvp.name} is the MVP of the Tournament with {
              mvp.points} points.")

    def show_player_statistics(self):
        # Prompt the user to choose a team
        team = self.choose_team()

        # Prompt the user to choose a player from the selected team
        player = self.choose_player(team)

        # Convert the player object to a dictionary using the to_dict method
        player_stats = player.player_to_dict()

        # Print the statistics for the selected player in the selected team
        print(f"\nStatistics for {player.name} in {team.name} Team:\n")

        # Iterate over each stat and value in the player_stats dictionary
        for stat, value in player_stats.items():
            # Exclude the 'name' and 'position' stats from being printed
            if stat != 'name' and stat != 'position':
                # Print the capitalized stat name and its corresponding value
                print(f"\t{stat.capitalize()}: {value}")
