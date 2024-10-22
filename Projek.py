#projek untuk menghitung berapa hari lagi sampai ulang tahun

import datetime 
from datetime import date
def sapa (person):
    print("Hello", person)
    print("Nice to meet you", person)
    feeling = int(input("How old are you ? "))
    print ("Ohh, so", person, "is", feeling, "years old")
    print ("So you where born on", 2024 - feeling)

sapa("Marco")

birthday = input("when do you born? (yyyy-MM-DD)")
today = date.today()
y = date.fromisoformat (birthday)
x = abs(today - y) #abs buat bikin angka yang dikasih jadi bulet absolute value
print ("So it's been", x.days, "days")

