from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("./drivers/chromedriver108",
                          options=options)  # Check chrome version
page = 1


def appendnews(link):
    all_news = []  # List to store name of the new
    links = []  # List to store price of the product
    images = []  # List to store rating of the product
    titles = []  # List to store rating of the product

    print(f"Scrapping: {link}")
    driver.get(link)  # endpoint/url onde vamos pegar os dados
    content = driver.page_source  # source/conteudo retornado
    # print(content)
    soup = BeautifulSoup(content, features="html.parser")
    # print(soup)
    for div in soup.findAll('div', attrs={'class': 'line'}):
        global page
        # transform inner loop content into function
        imgItem = div.find('img')
        newsContainer = div.find('div', attrs={'class': 'title'})
        a = newsContainer.find('a', href=True)
        title = a.text
        imgSrc = imgItem.get('src')
        link = a.get('href')
        # Transform this into a class
        news = {
            "img": imgSrc,
            "title": title,
            "link": link,
        }

        all_news.append(news)
        images.append(imgSrc)
        titles.append(title)
        links.append(link)

    today = datetime.now()
    category = "generalista"
    filename = f'files/news_{category}_{today.year}_{today.month}_{today.day}_{page}.csv'
    df = pd.DataFrame({'Image': images, 'Title': titles, 'link': links})
    df.to_csv(filename, index=False, encoding='utf-8')
    page += 1

    nextPage = soup.find('a', href=True, attrs={'class': 'right'})
    if nextPage:
        appendnews(nextPage.get('href'))
        # imgContainer = div.find('div', attrs={'class': 'small_headline_thumb'})
        # linkContainer = imgContainer.find('a', href=True)
        # img = imgContainer.find('img')


appendnews("https://www.angonoticias.com/Artigos/canal/2/generalista")

# today = datetime.now()
# category = "generalista"
# filename = f'news_{category}_{today.year}_{today.month}_{today.day}.csv'
# df = pd.DataFrame({'Image': images, 'Title': titles, 'link': links})
# df.to_csv(filename, index=False, encoding='utf-8')
# print("DONE")
# <div class = "small_headline" >
# <div class = "small_headline_thumb" >
# <a href = "https://www.angonoticias.com/Artigos/item/72687/sonangol-lanca-concurso-internacional-para-importacao-de-combustiveis" >
# <img alt = "" src = "https://www.angonoticias.com/site/assets/uploads/images/20230109111913_thumb.jpg"/>
# < /a >
# </div >
# <div class = "small_headline_title" > <a href = "https://www.angonoticias.com/Artigos/item/72687/sonangol-lanca-concurso-internacional-para-importacao-de-combustiveis" > Sonangol lança concurso internacional para... < /a > </div >
# </div >

# <div class = "small_headline_title" >
# <a href = "https://www.angonoticias.com/Artigos/item/72685/publicidade-de-bebidas-alcoolicas-em-locais-proibidos-e-o-que-mais-viola-a-lei" > Publicidade de bebidas alcoólicas em locais... < /a >
# </div >
