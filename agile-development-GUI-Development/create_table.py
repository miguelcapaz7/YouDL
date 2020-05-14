import sqlite3

conn = sqlite3.connect('youtube.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE YouTubeVideo
          (id INTEGER PRIMARY KEY ASC, 
           title TEXT NOT NULL,
           author TEXT NOT NULL,
           resolution TEXT NULL,
           frame_rate TEXT NULL,
           pathname TEXT NOT NULL,
           filename TEXT NOT NULL)
          ''')

conn.commit()
conn.close()