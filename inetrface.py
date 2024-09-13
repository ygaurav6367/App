from tkinter import *
df = Tk()
df.title("Whetather App")
import requests
import json

img= PhotoImage(file=r"D:\Downloads\wth2.png")
l2=Label(df,image=img)
l2.place(x=570,y=10)

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
cloud_l5.place(x=180,y=50)

bg= PhotoImage(file=r"D:\Downloads\Ws.png")
bg_l5=Label(df,image=bg)
bg_l5.place(x=1200,y=50)

wind_info= PhotoImage(file=r"D:\Downloads\apa3a5ab1.png")
wind_l6=Label(df,image=wind_info)
wind_l6.place(x=1190,y=270)

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



Entry_box=Entry(font=("Arial",25),bg="white",fg="black",textvariable=v)
Entry_box.place(x=585,y=350)

Entry_box.bind("<Return>",wheather_status)

txt=Label(df,font=("Arial Black",12),text="Please, Enter Here Your City Name : ",fg="black")
txt.place(x=220,y=360)

txt1=Label(df,font=("Broadway",20),text="Current Wheather information",fg="black")
txt1.place(x=60,y=205)

txt2=Label(df,font=("Broadway",20),text="Real-time Weather API",fg="black")
txt2.place(x=1115,y=205)

txt3=Label(df,font=("Calibari",11),text="* Note : Click on Submit / Press Enter ",fg="Red")
txt3.place(x=630,y=458)

Btn= Button(df, font=("Arial Black",12),text="Submit",fg="orange",bg="skyblue",command=wheather_status)
Btn.place(x=720,y=415)

temp_r=Label(df,font=("Arial Black",15),text="Tempreture in Region",fg="black")
temp_r.place(x=300,y=490)

show_r=Label(df,font=("Arial",15),text=" ",fg="red")
show_r.place(x=380,y=530)

temp_f=Label(df,font=("Arial Black",15),text="Tempreture in Fahrenheit (°F)",fg="black")
temp_f.place(x=600,y=490)

show_f=Label(df,font=("Arial",15),text=" ",fg="red")
show_f.place(x=740,y=530)

temp_c=Label(df,font=("Arial Black",15),text="Tempreture in Celsius (°C)",fg="black")
temp_c.place(x=970,y=490)

show_c=Label(df,font=("Arial",15),text=" ",fg="red")
show_c.place(x=1090,y=530)

ws=Label(df,font=("Arial Black",15),text="Wind Speed (Kph)",fg="black")
ws.place(x=320,y=580)

show_ws=Label(df,font=("Din",15),text=" ",fg="green")
show_ws.place(x=400,y=620)

w_a=Label(df,font=("Arial Black",15),text="Wind Angle (°)",fg="black")
w_a.place(x=690,y=580)

show_wa=Label(df,font=("Din",15),text=" ",fg="green")
show_wa.place(x=740,y=620)

w_d=Label(df,font=("Arial Black",15),text="Wind Direction",fg="black")
w_d.place(x=1035,y=580)

show_wd=Label(df,font=("Din",15),text=" ",fg="green")
show_wd.place(x=1095,y=620)

dt=Label(df,font=("Arial",12),text="Last Updated : ",fg="black")
dt.place(x=1230,y=755)

show_dt=Label(df,font=("Din",12),text=" ",fg="red")
show_dt.place(x=1340,y=755)

df.mainloop()
