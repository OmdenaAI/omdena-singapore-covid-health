import requests
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')

def get_soup(url):
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    return soup

def timesofindia():
    links = []
    with open('article_link.txt', 'r') as text:
        links.append(text.readlines())

    with open('DV_tof.csv', 'w', newline='') as file:
            fieldnames = ['url', 'title', 'article']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            counter = 0
            for link in links[0][1:]:
                soup = get_soup(link)
                title = soup.find('h1', {'class': 'K55Ut'})
                article = soup.find('div', {'class': '_3WlLe'})
                try:
                    total_desc = {'url': link, 'title': title.text, 'article': article.get_text()}
                    writer.writerow(total_desc)
                except:
                    pass
                counter+=1
                print(counter)
                # try:
                #     print(title.text, '\n', article.get_text())
                # except:
                #     pass
                # counter += 1
                # if counter == 3:
                #     browser.close()
                #     break



#     for page in range(1, 16):
#         url = f"{NEWS_SITE}/topic/domestic-violence/{page}"
#         soup = get_soup(url)

#         for litag in soup.find_all('li', {'class': 'article'}):
#             for divtag in litag.find_all('div', {'class': 'content'}):
#                 news_article_link = NEWS_SITE + divtag.find('a')['href']
#                 article_soup = get_soup(news_article_link,)
# #                 print(article_soup)
#                 title = article_soup.find_all('h1', {'class': 'K55Ut'})
#                 article = article_soup.find_all('div', {'class': '_3WlLe'})
#                 print(title, article)
#                 # browser.close()
                
#         break
if __name__ == '__main__':
    timesofindia()
    browser.close()