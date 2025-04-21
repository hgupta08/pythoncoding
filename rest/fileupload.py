# import requests
# myurl = 'https://httpbin.org/post'
# files = {'file': open('test.txt', 'rb')}
# getdata = requests.post(myurl, files=files)
# print(getdata.text)

import requests
cookies = {
    'test' :'test123'
}
getdata = requests.get('https://httpbin.org/cookies',cookies=cookies)
print(getdata.text)


import requests
req = requests.Session()
req.headers.update({'x-user1': 'ABC'})
headers = {'x-user2': 'XYZ'}
getdata = req.get('https://httpbin.org/headers', headers=headers)
print(getdata.headers)
