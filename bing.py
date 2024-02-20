import g4f


def summarizeNews(title, cookies):
  print(cookies)
  searchQuery = "rangkum berita dalam beberapa poin mengenai '" + title + "' ?"
  response = g4f.ChatCompletion.create(
      model=g4f.models.gpt_4,
      messages=[{"role": "user", "content": searchQuery}],
      provider=g4f.Provider.Bing,
      cookies=cookies
  )  
  return(response)