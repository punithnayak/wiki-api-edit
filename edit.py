import os
import requests
import time

S = requests.Session()

# ADD YOUR USERNAME HERE
S.headers.update({
    'User-Agent': 'test-bot/meta.wikimedia.org/wiki/User:EXAMPLE'
})

URL = 'https://meta.wikimedia.org/w/api.php'

PARAMS_0 = {
    'action': 'query',
    'meta': 'tokens',
    'type': 'login',
    'format': 'json'
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: POST request to log in. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    'action': 'login',
    'lgname': 'KCVelaga',
    'lgpassword': os.environ['WIKI_BOT_PASSWORD'],
    'lgtoken': LOGIN_TOKEN,
    'format': 'json'
}

R = S.post(URL, data=PARAMS_1)
print('Login:', R.json()['login']['result'], '-', R.json()['login'].get('reason'))
time.sleep(3)

PARAMS_2 = {
    'action': 'query',
    'meta': 'tokens',
    'format': 'json'
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']
print('CSRF:', 'ok' if CSRF_TOKEN != '+\\' else 'anonymous')
time.sleep(3)

PAGE_TITLE = 'User:EXAMPLE/sandbox'
APPEND_TEXT = '\n\n\nThis text was appended via the API.'

PARAMS_3 = {
    'action': 'edit',
    'title': PAGE_TITLE,
    'appendtext': APPEND_TEXT,
    'summary': 'Appending text via API',
    'token': CSRF_TOKEN,
    'format': 'json'
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()
print('Edit:', DATA.get('edit', DATA.get('error')))
time.sleep(3)

PARAMS_4 = {
    'action': 'logout',
    'token': CSRF_TOKEN,
    'format': 'json'
}

R = S.post(URL, data=PARAMS_4)
print('Logout status:', R.status_code)

S.close()
