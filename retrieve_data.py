import requests
from match import Match

url = 'https://api.octane.gg/api/matches/?sort=&page=1'


def create_match(match_data):
    match = Match(match_data['Team1'], match_data['Team2'], match_data['Team1Games'], match_data['Team2Games'], match_data['Date'], match_data['Time'], match_data['Event'])
    return match


def print_to_csv(matches, filename):
    f = open(filename, 'w')
    headers = 'Event, Team 1, Team 1 Wins, Team 2, Team 2 Wins, Winner, Date, Time\n'
    f.write(headers)
    for match in matches:
        f.write(match.csv_output())


response = requests.get(url)
data = response.json()
per_page = data['per_page']
matches_data = data['data']
matches = []

for match in matches_data:
    matches.append(create_match(match))

for match in matches:
    match.print_match()

print_to_csv(matches, 'matches.csv')
