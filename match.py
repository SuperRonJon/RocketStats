class Match:
    def __init__(self, team1, team2, team1games, team2games, date, time, event):
        self.team1 = team1
        self.team2 = team2
        self.team1_games = team1games
        self.team2_games = team2games
        self.date = date
        self.time = time
        self.event = event.split('|')[0]
        self.winner = 'x'
        if(team1games > team2games):
            self.winner = team1
        else:
            self.winner = team2

    def csv_output(self):
        return self.event + ',' + self.team1 + ',' + str(self.team1_games) + ',' + self.team2 + ',' + str(self.team2_games) + ',' + self.winner + ',' + self.date + ',' + str(self.time) + '\n'

    def print_match(self):
        print(self.team1 + ' vs ' + self.team2 + ": " + self.winner + ' wins ' + str(self.team1_games) + '-' + str(self.team2_games))
