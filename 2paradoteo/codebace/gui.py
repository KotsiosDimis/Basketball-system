import tkinter as tk
from tkinter import ttk, messagebox
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

    def simulate_match(self, home_team, away_team):
        home_team_score = 0
        away_team_score = 0

        print(f"\n1. {home_team.name}\n")
        print(f"2. {away_team.name}\n")

        while home_team_score < 2 and away_team_score < 2:
            scoring_team = input("Enter the number of the team that scored  (1 or 2): ")

            if scoring_team == '1':
                home_player = self.choose_player(home_team)
                self.update_player_stats(home_player)
                home_team_score += home_player.points
                print(f"\t{home_player.name} scores {home_player.points} points. Total score: {home_team_score} - {away_team_score}")

            elif scoring_team == '2':
                away_player = self.choose_player(away_team)
                self.update_player_stats(away_player)
                away_team_score += away_player.points
                print(f"\t{away_player.name} scores {away_player.points} points. Total score: {home_team_score} - {away_team_score}")
            else:
                print("Invalid choice. Please try again.")

        return home_team_score, away_team_score

    def update_player_stats(self, player):
        player.points = self.get_points(f"Enter the number of points for {player.name}'s shot: ")
        player.assists += self.get_assists(f"Enter the number of assists for {player.name}: ")
        player.steals += self.get_steals(f"Enter the number of steals for {player.name}: ")

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

    def get_assists(self, message):
        while True:
            try:
                assists = int(input(message))
                if assists >= 0:
                    return assists
                else:
                    print("Invalid number of assists. Please enter a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_steals(self, message):
        while True:
            try:
                steals = int(input(message))
                if steals >= 0:
                    return steals
                else:
                    print("Invalid number of steals. Please enter a non-negative number.")
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

class JSONOperations:
    def __init__(self, filename):
        self.filename = filename

    def teams_to_dict(self, league):
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
        with open(self.filename, 'r+') as f:
            file_data = json.load(f)
            file_data.update({"teams": self.teams_to_dict(league)["teams"]})
            f.seek(0)
            json.dump(file_data, f, indent=4)
            f.truncate()

    def handle_json(self):
        with open(self.filename, "r") as file:
            data = json.load(file)

        teams = data["teams"]
        team_objects = []

        for team in teams:
            team_obj = Team(team["name"], team["city"], team["logo"])
            team_obj.wins = team["wins"]

            for player in team["players"]:
                player_obj = Player(player["name"], player["position"], team_obj)
                player_obj.points = player["points"]
                player_obj.rebounds = player["rebounds"]
                player_obj.assists = player["assists"]
                player_obj.steals = player["steals"]
                player_obj.blocks = player["blocks"]
                player_obj.fouls = player["fouls"]

                team_obj.players.append(player_obj)

            team_objects.append(team_obj)

        return team_objects

    def reset_numerical_values(self):
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
        if os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write('')
            print("Data cleared successfully.")
        else:
            print(f"Error: '{self.filename}' not found.")

class BasketballGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Basketball Simulation")

        self.main_frame = tk.Frame(root)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label = tk.Label(self.main_frame, text="Basketball Simulation", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.tree = ttk.Treeview(self.main_frame, columns=('Team', 'City', 'Wins'), show='headings', height=10)
        self.tree.heading('Team', text='Team')
        self.tree.heading('City', text='City')
        self.tree.heading('Wins', text='Wins')
        self.tree.grid(row=1, column=0, columnspan=3, pady=10)

        self.create_buttons()

        self.league = BasketballLeague([])
        self.file = JSONOperations('2paradoteo\\codebace\\basketball_data.json')

    def create_buttons(self):
        buttons_frame = tk.Frame(self.main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=3, pady=10)

        tk.Button(buttons_frame, text="Use Existing Data", command=self.use_existing_data).grid(row=0, column=0, padx=5)
        tk.Button(buttons_frame, text="Append New Data", command=self.append_new_data).grid(row=0, column=1, padx=5)
        tk.Button(buttons_frame, text="Reset All Values", command=self.reset_values).grid(row=0, column=2, padx=5)
        tk.Button(buttons_frame, text="Delete All Data", command=self.delete_data).grid(row=1, column=0, columnspan=3, pady=5)
        tk.Button(buttons_frame, text="Exit", command=self.root.destroy).grid(row=2, column=0, columnspan=3, pady=10)

    def use_existing_data(self):
        try:
            existing_teams = self.file.handle_json()
            self.league.teams.extend(existing_teams)
            self.update_treeview()
            self.run_championship()
        except FileNotFoundError:
            messagebox.showerror("Error", "'basketball_data.json' not found. Please choose Append New Data or Reset All Values.")

    def append_new_data(self):
        num_teams = int(input("Enter the number of teams that you want to add: "))
        self.league.create_teams(num_teams)
        num_players_per_team = int(input("\nEnter the number of players per team: "))
        for team in self.league.teams:
            self.league.create_players_for_team(team, num_players_per_team)
        existing_teams = self.file.handle_json()
        self.league.teams.extend(existing_teams)
        self.update_treeview()
        self.run_championship()

    def reset_values(self):
        self.file.reset_numerical_values()
        messagebox.showinfo("Success", "Numerical values reset successfully.")
        self.update_treeview()

    def delete_data(self):
        self.file.delete_data()
        self.root.destroy()

    def run_championship(self):
        self.league.create_championship()
        self.file.append_to_json_file(self.league)
        messagebox.showinfo("Success", "Championship completed. Check 'basketball_data.json' for results.")
        self.update_treeview()

    def show_stats_buttons(self):
        for team in self.league.teams:
            for player in team.players:
                button_assists = tk.Button(
                    self.main_frame,
                    text=f"Increment {player.name}'s Assists",
                    command=lambda p=player: self.increment_stat(p, 'assists')
                )
                button_assists.grid(row=3, column=0, pady=5)

                button_steals = tk.Button(
                    self.main_frame,
                    text=f"Increment {player.name}'s Steals",
                    command=lambda p=player: self.increment_stat(p, 'steals')
                )
                button_steals.grid(row=3, column=1, pady=5)

    def increment_stat(self, player, stat):
        value = int(input(f"Enter the number to increment {player.name}'s {stat}: "))
        if stat == 'assists':
            player.assists += value
        elif stat == 'steals':
            player.steals += value

        # After incrementing, update the treeview
        self.update_treeview()

    def update_treeview(self):
        # Clear the existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert updated data into the treeview
        for team in self.league.teams:
            self.tree.insert('', 'end', values=(team.name, team.city, team.wins))

if __name__ == "__main__":
    root = tk.Tk()
    app = BasketballGUI(root)
    root.mainloop()
