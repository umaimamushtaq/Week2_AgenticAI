import requests

import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("API_KEY")
URL=api_key+"1"

response=requests.get(URL)

print(response.status_code)

if(response.status_code==200):
    post=response.json()
    print("Post ID:", post["id"])
    print("Title:", post["title"])
    print("Body:", post["body"])
else:
    print("Request failed")