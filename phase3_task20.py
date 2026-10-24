import requests

import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("API_KEY")

URL=api_key

response=requests.get(URL)

if(response.status_code==200):
    print("Status code:",response.status_code)
    print("Request successful")

elif(response.status_code==401):
    print("Request Failed!")
    print("Status code:",response.status_code)
    print("Authentication required")

elif(response.status_code==404):
    print("Request Failed!")
    print("Status code:",response.status_code)
    print("Resource not found")

elif(response.status_code==429):
    print("Request Failed!")
    print("Status code:",response.status_code)
    print("Too many requests")

elif(response.status_code==500):
    print("Request Failed!")
    print("Status code:",response.status_code)
    print("Internal Server Error")

else:
    print("Something went wrong!")
    print("Status code:",response.status_code)
