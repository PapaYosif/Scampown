import requests
import os
from random import randint
import string
import json


url = 'https://spins-game.pw/auth'
names = json.loads(open('names.json').read())

while 1:
    for name in names:
        username = name+str(randint(1000,9999))
        password = names[randint(1,1000)]
        requests.post(url, allow_redirects=False, data={
		'login': username,
		'password': password
	    })
        print('username: '+username+'password: '+password+'url:'+url)
