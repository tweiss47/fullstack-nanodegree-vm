#
# Database access functions for the web forum.
#

import time
import psycopg2

DBNAME = 'forum'

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('SELECT content, time FROM posts ORDER BY time DESC')
    posts = c.fetchall()
    db.close()
    return posts


## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("INSERT INTO posts VALUES(%s)" % content)
    db.commit()
    db.close()

