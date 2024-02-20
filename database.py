from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

# Connect to your postgres DB
conn = psycopg2.connect(
  dbname=os.getenv('DB_NAME'), 
  user=os.getenv('DB_USER'), 
  password=os.getenv('DB_PASSWORD'), 
  host=os.getenv('DB_HOST'), 
  port=os.getenv('DB_PORT')
)

# Function to insert data into the table
def insertNews(data):
  if not data:
    return("Berita Sudah Ada Pada Database")
  cur = conn.cursor()
  query = "INSERT INTO news (title, link, time, image, category, source, summary, sentiment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
  values = (data['title'], data['link'], data['publish_date'], data['image'], data['category'], data['source'], data['summary'], data['sentiment'])
  cur.execute(query, values)
  # Commit the changes
  conn.commit()

  if cur.rowcount > 0:
    return("Berita Berhasil Ditambahkan")
  else:
    return("Berita Gagal Ditambahkan")

def checkExistingNews(title):
  cur = conn.cursor()
  query = "SELECT EXISTS(SELECT 1 FROM news WHERE title LIKE %s)"
  cur.execute(query, (title,))
  result = cur.fetchone()[0]
  return result

def checkSources(source):
  cur = conn.cursor()
  query = "SELECT * FROM news ORDER BY id DESC LIMIT 4"
  cur.execute(query)
  result = cur.fetchall()
  for row in result:
    if row[7] == source:
      return True
  return False