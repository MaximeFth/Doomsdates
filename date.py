import time as t
import datetime
import random


weekdays = {1:'Monday',2:'Tuesday',3:'Wednesday',4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"}
def gendate():
    start_date = datetime.date(1800, 1, 1)
    end_date = datetime.date(2200, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

if __name__ == "__main__":
    t1 = t.time()
    newdate = gendate()
    print(newdate)
    answer = input("Enter day:")
    answer = str(answer)
    while weekdays.get((newdate.weekday()+1)%7).upper() != answer.upper():
        print("Nope")
        answer = input("Enter day: ")
        answer = str(answer)
    t2 = t.time()
    print("**Congrats! Time: {:.2f}**".format(t2-t1))


