import requests
import os
from dotenv import load_dotenv
load_dotenv()

def Get_Weather_Details(lat,lon):
    url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude=hourly,daily&APPID={os.getenv('API_KEY')}"
    try:
        r=requests.get(url=url)
        return r.json()
    except Exception as e:
        return e