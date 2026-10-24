import requests

import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

URL=api_key

response=requests.get(URL)
posts=response.json()

print(response.status_code)
id=1

if(response.status_code==200):
    for post in posts:
        if(id<=3):
            URL="https://jsonplaceholder.typicode.com/posts/"+str(id)
            print("Post ID:", post["id"])
            print("Title:", post["title"])
            print("Body:", post["body"])
            print("")
            id+=1
else:
    print("Request failed")