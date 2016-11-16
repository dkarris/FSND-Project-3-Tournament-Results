import psycopg2
import random

names = [
    'Celina', 'Zulema', 'Natividad', 'Tyron',
    'Jc', 'Josette', 'Selene', 'Dione', 'Johnathon',
    'Simon', 'Leoma', 'Floy', 'Ann', 'Eugene', 'Mae',
    'Valery', 'Odelia', 'Santos', 'Melania', 'Roxann',
    'Madalyn', 'Crissy', 'Ivette', 'Carla', 'Dona',
    'Scarlett', 'Alleen', 'Kiera', 'Synthia', 'Cordia',
    'Asley', 'Florinda', 'Ryann', 'Anja', 'Kathrin', 'Nestor',
    'Gonzalo', 'Elliot', 'Hayden', 'Alison', 'Ed',
    'Yuri', 'Lynna', 'Willene', 'Lillia', 'Florentino',
    'Rodney', 'Kala', 'Laurel', 'Clark'
    ]

names_list = zip(range(len(names)),names)
conn = psycopg2.connect("dbname=test user=vagrant")
cur = conn.cursor()

# Delete previous matches table
cur.execute ("DROP TABLE games;")
#cur.execute ("DROP TABLE test;")


# Delete previous players table
cur.execute ("DROP TABLE players;")
cur.execute ('''
                CREATE TABLE players (
                id SERIAL PRIMARY KEY, name text);
            ''')
# Create players table
for element in names_list:
    cur.execute("INSERT INTO players (id, name) VALUES (%s, %s);",
                (element[0],element[1]))
   

# Create a new table
cur.execute ('''CREATE TABLE games (
             id SERIAL PRIMARY KEY,
             winner integer REFERENCES players(id),
             loser integer  REFERENCES players(id));
                        ''')

# Create random matches
matches = 20

number_of_players = len(names_list)-1
random.seed()
for x in range(0,matches):
    winner_id = random.randint(0,number_of_players)
    loser_id = random.randint(0,number_of_players)
    while winner_id == loser_id:
        loser_id = random.randint(0,number_of_players)
    cur.execute("INSERT INTO games (id, winner, loser) VALUES(%s, %s, %s);",
                (x, winner_id, loser_id))

conn.commit()
conn.close()





