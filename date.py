import time as t
import datetime
import random
import sqlite3

from rich.console import Console


weekdays = {1:'Monday',2:'Tuesday',3:'Wednesday',4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"}
console = Console()

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
    print(newdate)
    answer = input("Enter day:")
    answer = str(answer)
    while weekdays.get((newdate.weekday()+1)%7).upper() != answer.upper():
        tries += 1
        print("Nope")
        answer = input("Enter day: ")
        answer = str(answer)
    t2 = t.time()
    print("**Congrats! Time: {:.2f}**".format(t2-t1))
    addToDB(t2-t1,newdate,tries)


