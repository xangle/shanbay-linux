import requests
import re

authorize_url = 'https://api.shanbay.com/oauth2/authorize/'
authorize_args = {
    'client_id': '48494ff346ee67137b8c',
    'response_type': 'code',
    'state': '200'
}
get_oauth2 = requests.get(authorize_url, params=authorize_args)
code = int(re.search(r'\d+', re.search(r'code.+state', get_oauth2.url).group()).group())

token_url = 'https://api.shanbay.com/oauth2/token/'
token_args = {
    'client_id': '48494ff346ee67137b8c',
    'client_secret': 'fb8ff3ce5224383e1c3b63711b00121f29e2b5cb',
    'grant_type': 'implicit',
    'code': code,
    'redirect_uri': 'https://api.shanbay.com/oauth2/auth/success/'
}
post_oauth2 = requests.post(token_url, params=token_args)
print(post_oauth2.json)
print(">>>> Code: %d" % code)
print(">>>> token['code']: %d" % token_args['code'])
print(">>>> post_oauth2.url: %s" % post_oauth2.url)
print(">>>> get_oauth2.status: %d" % get_oauth2.status)
