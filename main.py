import time

from news import getRawNews, getNewsFromAllSources
from database import insertNews, checkExistingNews, checkSources
from bing import summarizeNews
from sentiment.main import checkSentiment
from category import categorize

# result = getRawNews('okezone')
cookies = [
  {"MUID":"0CC7BCB8AEF0639D20CAA89AAFAB622C","SRCHS":"PC","SRCHD":"AF","SRCHUID":"V","ipv6":"hit","SRCHUSR":"DOB","ANON":"A","NAP":"V","PPLState":"1","_U":"1qK9PYHOnB0iaX2jr3TtiSTljXosowPeyaGVUFiWwljFHgJ8Qvg76WJ_RFBes4DI30nqruEDo7cppeW4sUxObh8qnD7hNm89W7wNAY-exhve64ZMMR-M_CZHNK8rlBEfTkbAJKoXM9UVFskXIrgVyZb8tmMtp1AO9ysiSVDb8d5xkDtKKfDuej4Vq1uy85jPsZrqorCkoQg5nQcOBDtqdDA","WLS":"C","_SS":"PC","_RwBf":"r","dsc":"order","GC":"2JHHRP0bc0HbtHZhO-xUI3ZDR-FDKTfAKF44mlOfVDAx1PVW8DMB4t5YWlhFt4jZJIpvVWzkd5OmdH6t2AfoOg","cct":"aGOCdEuPiNUWWNpHbe3TmVRP1IA5AP4u3skSlS8603fWcWtcdhfQfU-vXqS3m3A7DNvlIqvmilPRUsTHHlalQw","SRCHHPGUSR":"SRCHLANG"},
  {"MUID":"3224DE84D442694D0CD5CD01D51468EE","SRCHD":"AF","SRCHUID":"V","ANON":"A","PPLState":"1","_uetvid":"ac0fb9b06e0d11ee98a413fde72fb34c","ABDEF":"V","MSPTC":"BQmNpFlM87yh1ctd9RIJHl7nWluXYzpPCMzOQNIJozo","MMCASM":"ID","WLS":"C","SRCHS":"PC","_SS":"SID","_clck":"eokvdg%7C2%7Cfj2%7C0%7C1483","_U":"1gFFvh8UoeS5Wusv5Fc34Q1UXb0nWStaLXCwNgMwbtf5Cf9pN9zI0Im7eB6TeQXdHCTEQfUmmCtENOPlKCCmow7PBSN0Qc3XmRDd1o6V6Hn2ORO0UNR2O7nWh55zj6ORT2fkJhUYtdKqgMXTdI1qOLNwWKWOv7UQp8aJVEY9yWXVuCL9u3XLzDcluILwLUterB3aHEX-69JUAclDqdMyvyA","SRCHUSR":"DOB","_RwBf":"r","SRCHHPGUSR":"SRCHLANG","ipv6":"hit","_clsk":"18tga96%7C1707291655923%7C2%7C1%7Co.clarity.ms%2Fcollect","GC":"CC352AsoGcrfDqCzK1ATr93BwWwLPEyFd9_Rklv3eK28gYwwzRBPAgfaiEbzI7ko36AAZDgmwn4SFbBXO2ntaQ"}
]

counter = 0

def generateOneNews(item):
  if checkExistingNews(item[0]['title']):
    return False
  
  title = item[0]['title']
  link = item[0]['link']
  publish_date = item[0]['isoDate']
  image = item[0]['image']
  category = categorize(item[0]['title'])
  if isinstance(image, dict):
    image = image.get('large', image.get('small', image))
  summary = summarizeNews(item[0]['title'], cookies[0])
  sentiment = checkSentiment(summary)
  return {
    'title': title,
    'link': link,
    'publish_date': publish_date,
    'image': image,
    'category': category,
    'summary': summary,
    'sentiment': sentiment
  }

def generateNews():
  for item in getNewsFromAllSources():
    global counter
    # if current title exist, skip this iteration
    if checkSources(item['source']):
      continue
    if checkExistingNews(item['title']):
      continue
    
    title = item['title']
    link = item['link']
    publish_date = item['isoDate']
    image = item['image']
    category = categorize(item['title'])
    source = item['source']
    if isinstance(image, dict):
      image = image.get('large', image.get('small', image))
    summary = summarizeNews(item['title'], cookies[counter % 2])
    counter += 1
    sentiment = checkSentiment(item['title'])

    mapped = {
      'title': title,
      'link': link,
      'publish_date': publish_date,
      'image': image,
      'category': category,
      'source': source,
      'summary': summary,
      'sentiment': sentiment
    }
    status = insertNews(mapped)
    yield status
    time.sleep(300)  # Add one minute delay

# cara pakai fungsinya

for status in generateNews():
  print(status)
