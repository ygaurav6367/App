from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
df = Tk()
df.title("Whetather App")
import requests
import json

img= PhotoImage(file=r"D:\Downloads\n581fpen1.png")
l2=Label(df,image=img)
l2.place(x=620,y=75)

wind_dir= PhotoImage(file=r"D:\Downloads\sj9carua.png")
wind_l1=Label(df,image=wind_dir)
wind_l1.place(x=1060,y=665)

wind_speed= PhotoImage(file=r"D:\Downloads\sejf60kef.png")
wind_l2=Label(df,image=wind_speed)
wind_l2.place(x=350,y=660)

wind= PhotoImage(file=r"D:\Downloads\wind-logo-png-transparent.png")
wind_l3=Label(df,image=wind)
wind_l3.place(x=40,y=590)

wind_degree= PhotoImage(file=r"D:\Downloads\dzmzfs0u.png")
wind_l4=Label(df,image=wind_degree)
wind_l4.place(x=700,y=660)

cloud= PhotoImage(file=r"D:\Downloads\y1sj30qt1.png")
cloud_l5=Label(df,image=cloud)
cloud_l5.place(x=180,y=80)

bg= PhotoImage(file=r"D:\Downloads\Ws.png")
bg_l5=Label(df,image=bg)
bg_l5.place(x=1200,y=80)

wind_info= PhotoImage(file=r"D:\Downloads\apa3a5ab1.png")
wind_l6=Label(df,image=wind_info)
wind_l6.place(x=1190,y=300)

humidity_img= PhotoImage(file=r"D:\Downloads\dew.png")
humidity_l7=Label(df,image=humidity_img)
humidity_l7.place(x=1370,y=570)

weather_info= PhotoImage(file=r"D:\Downloads\5zzdx0mk.png")
waether_l8=Label(df,image=weather_info)
waether_l8.place(x=1360,y=670)


v=StringVar()

def wheather_status(event=None):
    city=v.get()
    url = "https://api.weatherapi.com/v1/current.json?key=31bd569cac48441a97972805243008&q="+city
    df=requests.get(url)
    data = json.loads(df.content)
    show_r.config(text=str(data["location"]["region"]))
    show_c.config(text=str(data["current"]["temp_c"]))
    show_f.config(text=str(data["current"]["temp_f"]))
    show_ws.config(text=str(data["current"]["wind_kph"]))
    show_wa.config(text=str(data["current"]["wind_degree"]))
    show_wd.config(text=str(data["current"]["wind_dir"]))
    show_dt.config(text=str(data["current"]["last_updated"]))
    show_country.config(text=str(data["location"]["country"]))
    show_humidity.config(text=str(data["current"]["humidity"]))


    condition_text = data["current"]["condition"]["text"]
    icon_url = "https:" + data["current"]["condition"]["icon"]
    response = requests.get(icon_url)
    photo = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))   
    show_climate.config(image=photo)
    show_climate_text.config(text=condition_text)
    show_climate.image = photo


Entry_box=Entry(font=("Arial",25),bg="white",fg="black",textvariable=v)
Entry_box.place(x=585,y=350)

Entry_box.bind("<Return>",wheather_status)

txt=Label(df,font=("Arial Black",12),text="Please, Enter Here Your City Name : ",fg="black")
txt.place(x=220,y=360)

txt1=Label(df,font=("Broadway",20),text="Current Wheather information",fg="black")
txt1.place(x=60,y=235)

txt2=Label(df,font=("Broadway",20),text="Real-time Weather API",fg="black")
txt2.place(x=1115,y=235)

txt3=Label(df,font=("Calibari",11),text="* Note : Click on Submit / Press Enter ",fg="Red")
txt3.place(x=630,y=458)

Btn= Button(df, font=("Arial Black",12),text="Submit",fg="darkorange",bg="skyblue",command=wheather_status)
Btn.place(x=720,y=415)

temp_r=Label(df,font=("Arial Black",15),text="Region",fg="black")
temp_r.place(x=360,y=490)

show_r=Label(df,font=("Arial",15),fg="darkorchid",)
show_r.place(x=360,y=530)

temp_f=Label(df,font=("Arial Black",15),text="Tempreture in Fahrenheit (°F)",fg="black")
temp_f.place(x=600,y=490)

show_f=Label(df,font=("Arial",15),text=" ",fg="darkorchid")
show_f.place(x=740,y=530)

temp_c=Label(df,font=("Arial Black",15),text="Tempreture in Celsius (°C)",fg="black")
temp_c.place(x=970,y=490)

show_c=Label(df,font=("Arial",15),text=" ",fg="darkorchid")
show_c.place(x=1090,y=530)

ws=Label(df,font=("Arial Black",15),text="Wind Speed (Kph)",fg="black")
ws.place(x=320,y=580)

show_ws=Label(df,font=("Din",15),text=" ",fg="darkorange2")
show_ws.place(x=400,y=620)

w_a=Label(df,font=("Arial Black",15),text="Wind Angle (°)",fg="black")
w_a.place(x=690,y=580)

show_wa=Label(df,font=("Din",15),text=" ",fg="darkorange2")
show_wa.place(x=740,y=620)

w_d=Label(df,font=("Arial Black",15),text="Wind Direction",fg="black")
w_d.place(x=1035,y=580)

show_wd=Label(df,font=("Din",15),text=" ",fg="darkorange2")
show_wd.place(x=1095,y=620)

country=Label(df,font=("Arial Black",15),text="Country",fg="black")
country.place(x=130,y=490)

show_country=Label(df,font=("Arial",15),fg="darkorchid")
show_country.place(x=138,y=530)

temp_h=Label(df,font=("Arial Black",15),text="Humidity (%)",fg="black")
temp_h.place(x=1340,y=490)

show_humidity=Label(df,font=("Arial",15),text=" ",fg="darkorchid")
show_humidity.place(x=1390,y=530)

blank_body=Label(df,bg="darkorchid",width=600,height=5)
blank_body.pack()

blank_body_text=Label(df,font=("Arial Black",25),text="WEATHER FORECASTING APP",width=60,justify="center",bg="darkorchid",fg="orange")
blank_body_text.place(x=120,y=16)

dt=Label(df,font=("Din",12,"bold"),text="Last Updated : ",fg="white",bg="darkorchid")
dt.place(x=1267,y=8)

show_dt=Label(df,font=("Din",12,"bold"),text=" ",fg="orange",bg="darkorchid")
show_dt.place(x=1383,y=8)


show_climate_text=Label(df,font=("Arial",12,"bold"),bg="darkorchid",fg="orange")
show_climate_text.place(x=120,y=25)

climate_info=Label(df,font=("calibari",8,"bold"),text="👆Show Climate Changes Here👆",bg="darkorchid",fg="white")
climate_info.place(x=30,y=62)

show_climate=Label(df,bg="darkorchid")
show_climate.place(x=40,y=0)

df.mainloop()
