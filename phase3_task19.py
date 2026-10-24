import requests

import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

URL=api_key+"101"

response=requests.get(URL)

if(response.status_code==404):
    print("Request Failed!")
    print("Status code:",response.status_code)
    print("Resource not found")

