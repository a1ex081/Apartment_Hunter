from bs4 import BeautifulSoup
from requests import get
import time
from my_filter import address_extract, link_extract
import re
from selenium import webdriver

def main_loop(test): 

    if test == False:
        
        price = []
        address = []
        details = []
        overlay = []
        links = []
        baths, rooms, sqft, type_ = [], [], [], []

        headers = ({'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-Us, en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})

        cities = ['Long-Beach', 'Downey', 'Paramount', 'Bellflower', 'Whittier', 'Lakewood', 'Norwalk', 'South-Gage', 'Los-Alamitos', 'Cypress', 'Signal-HIll', 'Compton', 'Lynwood', 'Cerritos', 'Carson']

        sample = 'Long-Beach'

        try: 
            
            #for city in range(len(sample)):

            driver = webdriver.Firefox()

            base_site = 'https://www.zillow.com/{}-ca'.format(sample)

            driver.get(base_site)

            scroll_pause = 0.5
            last_height = driver.execute_script('return document.body.scrollHeight')
            while True:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(scroll_pause)
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height == last_height:
                    break
                last_height=new_height

            html_soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            
            #response = get(base_site, headers = headers)
            #html_soup = BeautifulSoup(response.text, 'html.parser')

            price += html_soup.find_all('div', class_= 'list-card-price')
            address += html_soup.find_all('address', class_= 'list-card-addr')
            details += html_soup.find_all('ul', class_= 'list-card-details')
            #overlay += html_soup.find_all('div', class_= 'list-card-variable-text list-card-img-overlay')
            #links += html_soup.find_all('a', class_= 'list-card-link list-card-link-top-margin list-card-img') 

            time.sleep(5)
        except:
            
            print('\nSomething whent terribly wrong somewhere\n')

        # Link extract test
        link_count = 0
        """
        for link in range(len(links)):
            
            print('link: {}'.format(links[link]))
            l = re.search(r"homedetails(.+?)zpid", str(links[link]))
            print('\n')
            print('{}'.format(l.text))
            link_count += 1

        print('link count: {}'.format(link_count))
        """
        # Details extract test
        
        count = 0
        driver.quit()
        for x in range(len(details)):

            print('Price: {}; Address: {}; Details: {}'.format(price[x].text, address[x].text,details[x].text))
            print('Raw details: {}'.format(details[x].text))
            count += 1

        print('\nTotal number of properties found: {}'.format(count))

        """"count2 = 0
        for detail in range(len(details)):
            
            count2 += 1
            rooms, baths, sqft, type_ = address_extract(details[detail].text)
        print('\nDetails extracted: {}\n'.format(count2))
        """

    else:

        print('\nTest is False\n')

def test():

    
    driver = webdriver.Firefox()

    url = 'https://www.google.com'

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    print(soup.prettify())

def main():
    
    test = False

    main_loop(test)

    #test()

if __name__ =='__main__':
    main()
