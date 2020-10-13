import requests
import bs4
from telegram.ext import Updater , CommandHandler
import requests

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

url="https://www.cricbuzz.com/live-cricket-scores/30384/kxip-vs-mi-13th-match-indian-premier-league-2020"

def score(update,context):
  res = requests.get(url,headers=HEADERS)
  soup = bs4.BeautifulSoup(res.content, features='lxml')
  chat_id = update.message.chat_id
  title = soup.find("div",{"class":"cb-min-bat-rw"}).get_text().strip()
  print(title)
  context.bot.send_message(chat_id=chat_id,text=title)


def main():
    updater = Updater('725266096:AAFZPNpL-7Mvk-95QEwsYZBg7EtklED3wLI',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('score',score))
    updater.start_polling()
    updater.idle()
if __name__=='__main__':
  main()
