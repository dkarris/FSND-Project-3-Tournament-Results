#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("DB connection error")

def deleteMatches():
    """Remove all the match records from the database."""
    conn, cur = connect()
    cur.execute("DELETE FROM matches;")
    conn.commit()
    cur.close()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn, cur = connect()
    cur.execute("DELETE FROM players;")
    conn.commit()
    cur.close()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn, cur = connect()
    cur.execute("SELECT count(id) FROM players;")
    a = cur.fetchone()
    cur.close()
    conn.close()
    return a[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn,cur = connect()
    cur.execute ("INSERT INTO players(name) VALUES (%s);",(name,))
    conn.commit()
    cur.close()
    conn.close()
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, cur = connect()
    cur.execute ("SELECT * FROM standings;")
    a = cur.fetchall()
    cur.close()
    conn.close()
    return a

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn,cur = connect()
    cur.execute("INSERT INTO matches (winner,loser) VALUES(%s,%s)",(winner,loser))
    conn.commit()
    cur.close()
    conn.close()
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []
    a = playerStandings()
    if len(a) % 2 == 0:
# If even then proceed 
        for x in range(0,len(a),2):
            pairings.append((a[x][0],a[x][1],a[x+1][0],a[x+1][1]))
    else:
# Odd number of rows handler
        pass
    return pairings
