CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );

# update posts set content = 'cheese' where content like '%spam%'
# delete from posts where content like '%spam%'
