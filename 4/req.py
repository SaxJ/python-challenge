import requests
import re

next = '72758'
while True:
    params = {'nothing': next}
    resp = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php', params=params)
    print(resp.text)
    next = re.search(r'\d+', resp.text).group()
