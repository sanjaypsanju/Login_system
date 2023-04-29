import requests
url='https://stackoverflow.com/questions/tagged/python'
r=requests.get(url)
print(r.content)