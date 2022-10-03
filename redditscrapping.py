import requests

personal_use_script = 'cvubelfv0g5PXYiRhaI7Cg'
secret_token = 'Ie9ukcv-IrwwqAal35AKCXVQvHQDcg'

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
# auth = requests.auth.HTTPBasicAuth('<CLIENT_ID>', '<SECRET_TOKEN>')
auth = requests.auth.HTTPBasicAuth(personal_use_script, secret_token) # 

# here we pass our login method (password), username, and password
'''
data = {'grant_type': 'password',
        'username': '<USERNAME>',
        'password': '<PASSWORD>'}
'''
data = {'grant_type': 'password',
        'username': 'rohanvg3',
        'password': 'Ramxj#275'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'CourseRecommender/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

to_print = f'Access Token Value = {TOKEN} \n'
print(to_print)

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/UIUC/hot",
                   headers=headers)

# print(res.json())  # let's see what we get

num = 1
for post in res.json()['data']['children']:
        stuff = post['data']['title']
        to_pr = f'{num}: {stuff} \n'
        print(to_pr)
        num += 1

print ("hello")