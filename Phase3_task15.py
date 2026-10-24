import requests

URL="https://jsonplaceholder.typicode.com/posts/"

response=requests.get(URL)
posts=response.json()

print(response.status_code)
id=1

if(response.status_code==200):
    print("Number of responses:",len(posts))
    for post in posts:
        if(id<=5):
            print("Title:", post["title"])
            id+=1
else:
    print("Request failed")