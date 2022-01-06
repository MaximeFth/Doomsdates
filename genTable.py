import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("MyScores.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE scores (date text, chalDate text,  time real,tries real)''')

    con.commit()
    con.close()