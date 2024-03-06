import g4f
from dotenv import load_dotenv
import os

load_dotenv()

def summarizeNews(title, cookies):
  if(os.getenv('MODE') == 0):
    print('Start Summarizing News...')
    searchQuery = "rangkum berita dalam beberapa poin mengenai '" + title + "' ?"
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": searchQuery}],
        provider=g4f.Provider.Bing,
    )  
    return(response)
  else:
    print('Start Summarizing News...')
    searchQuery = "rangkum berita dalam beberapa poin mengenai '" + title + "' ?"
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": searchQuery}],
        provider=g4f.Provider.Bing,
        cookies=cookies
    )  
    return(response)