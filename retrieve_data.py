import requests

url = 'https://api.octane.gg/api/matches/?sort=&page=1'

response = requests.get(url)
data = response.json()
per_page = data['per_page']
matches = data['data']