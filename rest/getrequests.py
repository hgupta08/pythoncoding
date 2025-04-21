import requests
payload = {'postId': 1}
getdata = requests.get('https://jsonplaceholder.typicode.com/comments',
params = payload)
print(getdata.json())

args = {
    "foo1": "bar1",
    "foo2": "bar2"
}
data=requests.get(url='https://postman-echo.com/get',params=args)
print(data.json())


myurl = 'https://postman-echo.com/post'
myparams = {'name': 'ABC', 'email':'xyz@gmail.com'}
res = requests.post(myurl, data=myparams)
print(res.text)