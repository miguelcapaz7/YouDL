import sqlite3

conn = sqlite3.connect('youtube.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE YouTubeVideo
          ''')

conn.commit()
conn.close()