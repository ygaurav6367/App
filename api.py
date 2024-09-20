import requests
import json

url = "https://api.weatherapi.com/v1/current.json?key=31bd569cac48441a97972805243008&q="+ input("enter city : ")

df=requests.get(url)
data = json.loads(df.content)
print("celsius : ",data["current"]["temp_c"])
print("fernehite : ",data["current"]["temp_f"])
print("wind Speed :",data["current"]["wind_kph"])
print("wind degree : ",data["current"]["wind_degree"])
print("wind direction : ",data["current"]["wind_dir"])