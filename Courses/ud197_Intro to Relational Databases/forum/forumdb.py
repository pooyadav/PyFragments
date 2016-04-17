#
# Database access functions for the web forum.
# 

import time

## Database connection

# DB = []

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.
    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    request = "select time, content from posts order by time desc"
    cur.execute(request)
    DB = cur.fetchall()

    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    posts.sort(key=lambda row: row['time'], reverse=True)

    conn.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.
    Args:
      content: The text content of the new post.
    '''
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()

    t = time.strftime('%c', time.localtime())
    #DB.append((t, content))

    request = "insert into posts (time, content) value ('%s', '%s')" % (t, content)
    cur.execute(request)
    conn.commit()
    conn.close()


##
# update posts set content = 'cheese' where content = 'malicious...'