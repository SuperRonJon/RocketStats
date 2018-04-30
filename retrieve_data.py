import requests
from match import Match

base_url = 'https://api.octane.gg/api/matches/?sort=&page='


def create_match(match_data):
    match = Match(match_data['Team1'], match_data['Team2'], match_data['Team1Games'], match_data['Team2Games'], match_data['Date'], match_data['Time'], match_data['Event'])
    return match


def print_to_csv(matches, filename):
    f = open(filename, 'w')
    headers = 'Event, Team 1, Team 1 Wins, Team 2, Team 2 Wins, Winner, Date, Time\n'
    f.write(headers)
    for match in matches:
        f.write(match.csv_output())


def get_matches_from_page(page_number):
    url = base_url + str(page_number)
    response = requests.get(url)
    data = response.json()
    matches_data = data['data']
    if len(matches_data) == 0:
        return None
    else:
        page_matches = []
        for match in matches_data:
            page_matches.append(create_match(match))
        return page_matches


def get_all_matches():
    page = 1
    all_matches = []
    curr_matches = get_matches_from_page(page)
    while curr_matches is not None:
        all_matches.extend(curr_matches)
        page += 1
        curr_matches = get_matches_from_page(page)
    return all_matches


matches = get_all_matches()
print_to_csv(matches, 'matches.csv')
