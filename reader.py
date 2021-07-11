import psycopg2
conn = psycopg2.connect(dbname='titanic', user='postgres', password='postgres')
cur = conn.cursor()
cur.execute("""CREATE TABLE passengers(
    id integer,
    survived integer,
    class integer,
    name text,
    sex varchar(50),
    age varchar(50),
    sibsp integer,
    parch integer,
    ticket varchar(255),
    fare numeric NULL,
    cabin varchar(255) NULL,
    embarked varchar(50)
)
""")
with open(r'titanic.txt', 'r') as f:
    next(f)
    cur.copy_from(f, 'passengers', sep='|')

conn.commit()

def all_survived():
    cur.execute("SELECT name FROM passengers WHERE survived=1;")
    passengers = cur.fetchall()
    print(len(passengers))
    for i in passengers:
        print(i)

def percent(a, b):
    return a*100/b

def woman_1st_class():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE class=1 AND sex='female' AND survived=1;")
    survived_woman = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE class=1 AND sex='female';")
    all_woman = cur.fetchall()[0][0]
    return percent(survived_woman, all_woman)

def mans_under_20():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE class=3 AND sex='male' AND  age < '20' AND survived=1;")
    survived_man = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE class=3 AND sex='male' AND  age < '20';")
    all_man = cur.fetchall()[0][0]
    return percent(survived_man, all_man)

def passengers_of_2ndcl():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE class=2 AND age > '30' AND survived=1;")
    survived = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE class=2 AND age > '30';")
    everyone = cur.fetchall()[0][0]
    return percent(survived, everyone)

def Cherbourg():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE sex='female' AND class=2 AND embarked='C' AND survived=1;")
    woman = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE sex='female' AND class=2 AND embarked='C';")
    every_woman = cur.fetchall()[0][0]
    return percent(woman, every_woman)

def Siblings():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE sibsp > 0 AND survived=1;")
    survived_siblings = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE sibsp > 0;")
    all_siblings = cur.fetchall()[0][0]
    return percent(survived_siblings, all_siblings)

def Average():
    cur.execute("SELECT AVG(CAST(age AS FLOAT)) FROM passengers WHERE age > '0' AND survived=0;")
    average_people = cur.fetchall()
    print(average_people)

def port_which_has_chance():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE embarked='Q';")
    every_Q_port_passengers = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE embarked='Q' AND survived=1;")
    survived_Q_port_passengers = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE embarked='S';")
    every_S_port_passengers = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE embarked='S' AND survived=1;")
    survived_S_port_passengers = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE embarked='C';")
    every_C_port_passengers = cur.fetchall()[0][0]
    cur.execute("SELECT COUNT(*) FROM passengers WHERE embarked='C' AND survived=1;")
    survived_C_port_passengers = cur.fetchall()[0][0]
    dictionary_of_ports = {
        'Cherbourg': percent(survived_C_port_passengers, every_C_port_passengers),
        'Queenstown': percent(survived_Q_port_passengers, every_Q_port_passengers),
        'Southampton': percent(survived_S_port_passengers, every_S_port_passengers),
    }
    print(dictionary_of_ports)
    Port_Sir = None 
    the_most_lucky_one = max(dictionary_of_ports.values())
    for j in dictionary_of_ports:
        if dictionary_of_ports[j] == the_most_lucky_one:
            Port_Sir = j
    return Port_Sir

def who_is_Molly_Brown():
    cur.execute("SELECT name,survived FROM passengers WHERE sex='female' AND name ILIKE 'Brown%';")
    mrs = cur.fetchall()
    print(mrs)

all_survived()
print(f'{woman_1st_class():.2f}%')
print(f'{mans_under_20():.2f}%')
print(f'{passengers_of_2ndcl():.2f}%')
print(f'{Cherbourg():.2f}%')
print(f'{Siblings():.2f}%')
Average()
print(port_which_has_chance())
who_is_Molly_Brown()

cur.close()
conn.close()