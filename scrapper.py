from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

all_news = []  # List to store name of the new
links = []  # List to store price of the product
images = []  # List to store rating of the product
titles = []  # List to store rating of the product
driver = webdriver.Chrome("./drivers/chromedriver108") #Check chrome version
driver.get("https://www.angonoticias.com/") #endpoint/url onde vamos pegar os dados
content = driver.page_source #source/conteudo retornado
#print(content)
soup = BeautifulSoup(content)
# print(soup)
for div in soup.findAll('div', attrs={'class':'small_headline'}):
    #transform inner loop content into function
    imgItem = div.find('img')
    newsContainer = div.find('div', attrs={'class': 'small_headline_title'})
    a = newsContainer.find('a', href=True)

    title = a.text
    imgSrc = imgItem.get('src')
    link = a.get('href')
    #Transform this into a class
    news = {
        "img": imgSrc,
        "title": title,
        "link": link,
    }

    all_news.append(news)
    images.append(imgSrc)
    titles.append(title)
    links.append(link)
    # imgContainer = div.find('div', attrs={'class': 'small_headline_thumb'})
    # linkContainer = imgContainer.find('a', href=True)
    # img = imgContainer.find('img')

df = pd.DataFrame({'Image': images, 'Title': titles, 'link': links})
df.to_csv('news.csv', index=False, encoding='utf-8')
print(all_news)

# <div class = "small_headline" >
# <div class = "small_headline_thumb" > 
# <a href = "https://www.angonoticias.com/Artigos/item/72687/sonangol-lanca-concurso-internacional-para-importacao-de-combustiveis" > 
# <img alt = "" src = "https://www.angonoticias.com/site/assets/uploads/images/20230109111913_thumb.jpg"/> 
# < /a > 
# </div >
# <div class = "small_headline_title" > <a href = "https://www.angonoticias.com/Artigos/item/72687/sonangol-lanca-concurso-internacional-para-importacao-de-combustiveis" > Sonangol lança concurso internacional para... < /a > </div >
# </div >

#<div class = "small_headline_title" > 
# <a href = "https://www.angonoticias.com/Artigos/item/72685/publicidade-de-bebidas-alcoolicas-em-locais-proibidos-e-o-que-mais-viola-a-lei" > Publicidade de bebidas alcoólicas em locais... < /a > 
# </div >
