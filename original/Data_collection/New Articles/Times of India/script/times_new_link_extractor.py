import requests
from bs4 import BeautifulSoup


NEWS_SITE = 'https://timesofindia.indiatimes.com'

def get_soup(url):
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    return soup

def timesofindia():
    for page in range(1, 16):
        url = f"{NEWS_SITE}/topic/domestic-violence/{page}"
        soup = get_soup(url)

        for litag in soup.find_all('li', {'class': 'article'}):
            for divtag in litag.find_all('div', {'class': 'content'}):
                news_article_link = NEWS_SITE + divtag.find('a')['href']
                with open('article_link.txt', 'a') as text:
                    text.writelines(news_article_link+'\n') 
if __name__ == '__main__':
    timesofindia()