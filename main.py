import tkinter as tk
import json
import requests as req

cat = tk.Tk()


def btn_update():

    answer = entry.get()
    if answer == "A":
        display_answer.config(text="Alpha")
    elif answer == "a":
        display_answer.config(text="alpha")
    elif answer == "B":
        display_answer.config(text="Bravo")
    elif answer == "b":
        display_answer.config(text="bravo")
    elif answer == "C":
        display_answer.config(text="Charlie")
    elif answer == "c":
        display_answer.config(text="charlie")
    elif answer == "D":
        display_answer.config(text="Delta")
    elif answer == "d":
        display_answer.config(text="delta")
    elif answer == "E":
        display_answer.config(text="Echo")
    elif answer == "e":
        display_answer.config(text="echo")
    elif answer == "F":
        display_answer.config(text="Foxtrot")
    elif answer == "f":
        display_answer.config(text="foxtrot")
    elif answer == "G":
        display_answer.config(text="Golf")
    elif answer == "g":
        display_answer.config(text="golf")
    elif answer == "H":
        display_answer.config(text="Hotel")
    elif answer == "h":
        display_answer.config(text="hotel")
    elif answer == "I":
        display_answer.config(text="India")
    elif answer == "i":
        display_answer.config(text="india")
    elif answer == "J":
        display_answer.config(text="Juliet")
    elif answer == "j":
        display_answer.config(text="juliet")
    elif answer == "K":
        display_answer.config(text="Kilo")
    elif answer == "k":
        display_answer.config(text="kilo")
    elif answer == "L":
        display_answer.config(text="Lima")
    elif answer == "l":
        display_answer.config(text="lima")
    elif answer == "M":
        display_answer.config(text="Mike")
    elif answer == "m":
        display_answer.config(text="mike")
    elif answer == "N":
        display_answer.config(text="November")
    elif answer == "n":
        display_answer.config(text="november")
    elif answer == "O":
        display_answer.config(text="Oscar")
    elif answer == "o":
        display_answer.config(text="oscar")
    elif answer == "P":
        display_answer.config(text="Papa")
    elif answer == "p":
        display_answer.config(text="papa")
    elif answer == "Q":
        display_answer.config(text="Quebec")
    elif answer == "q":
        display_answer.config(text="quebec")
    elif answer == "R":
        display_answer.config(text="Romeo")
    elif answer == "r":
        display_answer.config(text="romeo")
    elif answer == "S":
        display_answer.config(text="Sierra")
    elif answer == "s":
        display_answer.config(text="sierra")
    elif answer == "T":
        display_answer.config(text="Tango")
    elif answer == "t":
        display_answer.config(text="tango")
    elif answer == "U":
        display_answer.config(text="Uniform")
    elif answer == "u":
        display_answer.config(text="uniform")
    elif answer == "V":
        display_answer.config(text="Victor")
    elif answer == "v":
        display_answer.config(text="victor")
    elif answer == "W":
        display_answer.config(text="Whiskey")
    elif answer == "w":
        display_answer.config(text="whiskey")
    elif answer == "X":
        display_answer.config(text="X-ray")
    elif answer == "x":
        display_answer.config(text="x-ray")
    elif answer == "Y":
        display_answer.config(text="Yankee")
    elif answer == "y":
        display_answer.config(text="yankee")
    elif answer == "Z":
        display_answer.config(text="Zulu")
    elif answer == "z":
        display_answer.config(text="zulu")
    elif answer == "1":
        display_answer.config(text="One")
    elif answer == "2":
        display_answer.config(text="Two")
    elif answer == "3":
        display_answer.config(text="Three")
    elif answer == "4":
        display_answer.config(text="Four")
    elif answer == "5":
        display_answer.config(text="Five")
    elif answer == "6":
        display_answer.config(text="Six")
    elif answer == "7":
        display_answer.config(text="Seven")
    elif answer == "8":
        display_answer.config(text="Eight")
    elif answer == "9":
        display_answer.config(text="Nine")
    elif answer == "10":
        display_answer.config(text="Ten")
    elif answer == "moo":
        display_answer.config(text="Super Invalid")
    elif answer == "Weather":
        response = req.get("https://goweather.herokuapp.com/weather/johannesburg")
        display_answer.config(text = response.json(), wraplengt=200)
    elif answer == "Funfact":
        response = req.get("https://api.aakhilv.me/fun/facts")
        display_answer.config(text = response.json(), wraplengt=200)
    elif answer == "Dogfact":
        response = req.get("http://dog-api.kinduff.com/api/facts")
        display_answer.config(text = response.json(), wraplengt=200)
    elif answer == "Spacex":
        response = req.get("https://api.spacexdata.com/v4/launches/latest")
        display_answer.config(text = response.json(), wraplengt=400)
    elif answer == "RBUF":
        response = req.get("https://uselessfacts.jsph.pl/random")
        display_answer.config(text = response.json(), wraplengt=400)
    else:
        display_answer.config(text="Invalid")


label = tk.Label(cat, text="Enter a letter or a number from 1 to 10")
display_answer = tk.Label(cat, text="")
entry = tk.Entry(cat)
label.pack()
entry.pack()
display_answer.pack()

tk.Button(cat, text="Enter", command=btn_update).pack()

cat.mainloop()
