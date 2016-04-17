#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from itertools import izip


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    req = "delete from match;"
    c.execute(req)
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    req = "delete * from player;"
    c.execute(req)
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    req = "select count(id) from player;"
    c.execute(req)
    row = c.fetchall()
    conn.commit()
    conn.close()
    return row[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    req = "insert into player (name) values (%s);"
    c.execute(req, (name,)) #in case of "O'Neil"
    conn.commit()
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
    conn = connect()
    c = conn.cursor()
    req0 = "select * from match;"
    c.execute(req0)
    if c.fetchone() == None:
        req0 = "select id, name, 0, 0 from player;"
        c.execute(req0)
        return list(c.fetchall)

    req1 = """
    select nt.id, player.name, 
    nt.wins, nt.m
    from (select id, sum(result) as wins, count(id) as m 
        from match group by id) as nt, player
    where nt.id = player.id
    order by nt.wins desc
    """
    c.execute(req1)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return list(rows)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    req1 = "insert into match (id, rival, result) values (%d, %d, 1);" % (winner, loser)
    req2 = "insert into match (id, rival, result) values (%d, %d, 0);" % (loser, winner)
    c.execute(req1)
    c.execute(req2)
    conn.commit()
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
    def pairwise(iterable):
        "s -> (s0, s1), (s2, s3), (s4, s5), ..."
        a = iter(iterable)
        return izip(a, a)

    ranking = playerStandings()
    ids = map(lambda t: t[0:2], ranking)
    # n = (len(ids) + 1) / 2
    result = []
    for a, b in pairwise(ids):
        result.append(a+b)
    return result