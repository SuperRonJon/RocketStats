class Match:
    def __init__(self, team1, team2, team1games, team2games, date, time, event):
        self.team1 = team1
        self.team2 = team2
        self.team1_games = team1games
        self.team2_games = team2games
        self.date = date
        self.time = time
        self.event = event.split('|')[0]
