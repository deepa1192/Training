import requests
r = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
print(r.json())
