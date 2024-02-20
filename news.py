import requests

sources = {
  'Antara': 'https://berita-indo-api-next.vercel.app/api/antara-news/terkini',
  'CNN': 'https://berita-indo-api-next.vercel.app/api/cnn-news',
  'CNBC': 'https://berita-indo-api-next.vercel.app/api/cnbc-news',
  'Republika': 'https://berita-indo-api-next.vercel.app/api/republika-news',
  'Okezone': 'https://berita-indo-api-next.vercel.app/api/okezone-news',
  'Kumparan': 'https://berita-indo-api-next.vercel.app/api/kumparan-news',
  'Vice': 'https://berita-indo-api-next.vercel.app/api/vice-news',
  'Suara': 'https://berita-indo-api-next.vercel.app/api/suara-news',
  'VOA': 'https://berita-indo-api-next.vercel.app/api/voa-news',
}

sourceArray = list(sources.keys())

def getRawNews(target):
  response = requests.get(sources[target])

  if response.status_code == 200:
    data = response.json()
    return data['data']
  else:
    return "Error:", response.status_code

def getNewsFromAllSources():
  i = 0
  print('Getting News from all sources...')
  while True:
    for source in sources:
      print('Getting News from ' + source + " : " + str(i))
      news = getRawNews(source)
      if i < len(news):
        news[i]['source'] = source
        yield news[i]
    i += 1
