import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

response_data =requests.get('httpbin.org/basic-auth/admin/admin123',
auth = HTTPDigestAuth('admin', 'admin123'))
print(response_data.text)

import requests
req = requests.Session()
cookies = dict(test='test123')
getdata = req.get('https://httpbin.org/cookies',cookies=cookies)
print(getdata.text)