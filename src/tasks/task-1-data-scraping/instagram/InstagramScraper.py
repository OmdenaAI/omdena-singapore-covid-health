import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import re
import json
import csv
import string

BASE_URL = "https://www.instagram.com/explore/tags"


class Scrapstagram:

    def __init__(self,hashtag,sleep_time=2,max_page=10):
        """
        Args:
            headless (str): Headless tool name.
            browser (str): Browser to run selenium.
            webdriver_path (str): Specific web driver path other than default.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.hashtag=hashtag
        self.max_page=max_page
        self.time=sleep_time
        self.driver = webdriver.Chrome('/Users/Shang/chromedriver') #options=chrome_options,executable_path=r"chromedriver.exe")


    def write_to_csv (self, data, file_name):
        print ('writing to CSV...')

        keys = data[0].keys()
        with open(file_name, 'a+',encoding='utf-8',newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print('written to file')

    def get_post_by_hashtag(self):
        """ Get post(s) by hashtags.
        Args:
            hashtag (str): Hashtag without '#'.
            max_page (int): Maximum page to scroll down on the web page before scrapping.
            max_post (int): Maximum number of post(s).
        Returns:
            list of post(s) dictionary with link, image, text, datetime, video, likes and views as keys.
        """

        # Navigate to the login page
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)

        time.sleep(30) #for logging-in and clearing obstacles to scraping

        # Navigate to the hashtag
        url = "{}/{}".format(BASE_URL, self.hashtag)
        self.driver.get(url)

        post = list()
        links={}

        # view the hashtag page and scroll the max_page
        for i in range(self.max_page):
            link_array = []

            for _ in range(5):
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(10) #self.time)
            print('success')

            # get links from the hashtag page and store it into an Array
            three_thumbnails = self.driver.find_elements_by_xpath("//div[@class='Nnq7C weEfm']")
            print(f'No. of total post {3*len(three_thumbnails)} in the page')

            if i >0:
                three_thumbnails = three_thumbnails[3:]
            for thumbnail in three_thumbnails:
                thumbnail_paths = thumbnail.find_elements_by_xpath('.//div[@class="v1Nh3 kIKUG  _bz0w"]')

                # get link
                for thumbnail_path in thumbnail_paths:
                    link = thumbnail_path.find_element_by_xpath('.//a').get_attribute("href")
                    link_array.append(link) # store link in the Link_Array

            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[1])

            # open pages and get data from it
            for link in link_array:

                # navigate to the link
                self.driver.get(link)
                time.sleep(10) #self.time)

                # get time

                user_name = self.driver.find_element_by_xpath('//div[@class="e1e1d"]').find_element_by_xpath('.//a').get_attribute("href")
                message = self.driver.find_element_by_xpath('//div[@class="C4VMK"]') # .find_element_by_xpath('.//a').get_attribute("href")
# another div class "eo2As  "
                if links.get(user_name,None) is None:

                    links[user_name] = True

                    print(user_name)
                    print(message)

                    r = requests.get(user_name)
                    time.sleep(self.time)
                    soup = BeautifulSoup(r.content,"html.parser")
                    scripts = soup.find_all('script', type="text/javascript", text=re.compile('window._sharedData'))
                    string1 = scripts[0].get_text().replace('window._sharedData = ', '')[:-1]
                    print(string1)
                    # d=json.loads(string1)['entry_data']['ProfilePage'][0]
                    # b=d['graphql']['user']
                    # s=b['biography']
                    # biography=''
                    # for e in s:
                    #     if (e.lower()  in string.ascii_lowercase) or (e is ' ')  or ( e=='\n'):
                    #         biography+=e

                    # data=dict(
                    #     fullname=b['full_name'],
                    #     handle=ele,
                    #     biography=biography,
                    #     website=b['external_url_linkshimmed'],
                    #     followers=b['edge_followed_by']['count'],
                    #     following=b['edge_follow']['count'],
                    #     user_id=b['id'],
                    #     is_business_account=b['is_business_account'],
                    #     business=b['business_category_name'],
                    #     is_private=b['is_private'],
                    #     is_verified=b['is_verified'],
                    # )
                    # post.append(data)


            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])


        self.driver.quit()
        return len(links),post


hashtag=input('Plzz input hashtag name without #:- ')
max_page=int(input('PlZz input pages to scrape:- '))
sleep_time=int(input('plzz input sleep time you wish to use for your program:-'))


web_dr=Scrapstagram(hashtag,max_page,sleep_time)
length,data=web_dr.get_post_by_hashtag()
print(length)
#filename=hashtag+'.csv'
#with open(filename,'w',encoding='utf-8') as output_file:
#    pass
#web_dr.write_to_csv(data,filename)
