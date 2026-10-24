import requests

import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("API_KEY")
URL=api_key+"1"

try:
    response=requests.get(URL, timeout=10)

    print(response.status_code)

    if(response.status_code==200):
        post=response.json()
        print("Post ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])
    else:
        print("Request failed")

except requests.exceptions.Timeout:
    print("Request timeout!")
    print("Request took more than 10 seconds")

except requests.exceptions.ConnectionError:
    print("Request failed!")
    print("Connection error")

except requests.exceptions.RequestException as e:
    print("Something went wrong!")
    print("API error")
    print(e)