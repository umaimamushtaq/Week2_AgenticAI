import requests

URL="https://jsonplaceholder.typicode.com/posts/1"

response=requests.get(URL)

print(response.status_code)

if(response.status_code==200):
    post=response.json()
    print("Post ID:", post["id"])
    print("Title:", post["title"])
    print("Body:", post["body"])
else:
    print("Request failed")