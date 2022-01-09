import time as t
import datetime
import random
import sqlite3
import calendar
from rich.console import Console
import numpy as np

weekdays = {1:'Monday',2:'Tuesday',3:'Wednesday',4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"}
console = Console()
def lcs(X, Y, m, n):
  
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
  
  
def closestTo(word):
    dists = []
    for i in range(7):
        dists.append(lcs(weekdays[i].lower(),word.lower(),len(weekdays[i]), len(word)))
    print(dists)
    return weekdays[np.argmax(dists)]


def dayToEng(myDate):
    date_suffix = ["th", "st", "nd", "rd"]

    if myDate % 10 in [1, 2, 3] and myDate not in [11, 12, 13]:
        return date_suffix[myDate % 10]
    else:
        return date_suffix[0]
def dateToEng(date):
    return f"{date.day}{dayToEng(date.day)} of {calendar.month_name[date.month]} {date.year}"
def gendate():
    start_date = datetime.date(1800, 1, 1)
    end_date = datetime.date(2200, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

def addToDB(time,date,tries):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    con = sqlite3.connect("MyScores.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO scores VALUES ('{now}','{date}','{time}', '{tries}')")
    con.commit()
    con.close()
    console.print("[+]", style = 'green', end='')
    console.print(" Score added to db succesfully.")
    return 

if __name__ == "__main__":
    tries=1
    t1 = t.time()
    newdate = gendate()
    print(dateToEng(newdate))
    answer = input("Enter day:")
    answer2 = str(answer)
    answer = closestTo(answer2)
    if(answer.upper() != answer2.upper()):
        console.print("[+]", style = 'green', end='')
        console.print(" Answer corrected: ",answer) 
    while weekdays.get((newdate.weekday()+1)%7).upper() != answer.upper():
        tries += 1
        print("Nope")
        answer = input("Enter day: ")
        answer = str(answer)
        answer = closestTo(answer)
    t2 = t.time()
    print("**Congrats! Time: {:.2f}**".format(t2-t1))
    addToDB(t2-t1,newdate,tries)


