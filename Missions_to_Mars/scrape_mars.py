from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager



def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    results = soup.find_all('div', class_="list_text")

    for result in results:
        news_title = result.find('div', class_="content_title").get_text()
        news_p = result.find('div', class_="article_teaser_body").get_text()

    url2 = "https://spaceimages-mars.com/"
    browser.visit(url2)
    html = browser.html
    soup2 = bs(html, "html.parser")
    images = soup2.find_all('img', class_="headerimage fade-in")
    image_src=[]
    featured_image_url= "https://spaceimages-mars.com/" + "image/featured/mars3.jpg"

    for image in images:
        s_image = image['src']
        image_src.append(s_image) 
    
    
    url3 = "https://galaxyfacts-mars.com/"
    browser.visit(url3)
    html = browser.html
    soup3 = bs(html, "html.parser")
    table = pd.read_html(url3)
    mars_facts_df = table[0]
    mars_facts_df.columns =  ["","Mars", "Earth"]
    mars_facts_df = mars_facts_df.iloc[1: , :]
    mars_facts_html_table = mars_facts_df.to_html()
    mars_facts_html_tableclean = mars_facts_html_table.replace("\n","")
    mars_table = mars_facts_html_tableclean

    hemisphere_image_urls = []
    url4 = "https://marshemispheres.com/cerberus.html"
    browser.visit(url4)
    html = browser.html
    soup4 = bs(html, "html.parser")
    results4 = soup4.find_all('body', id ="results")

    for result in results4:
        cerberus_title = soup4.find('h2', class_='title').text
        downloads = soup4.find('div', class_ = 'downloads')
        li = downloads.find('li')
        cerberus_img = li.find('a')['href']
        cerberus_img_url = 'https://marshemispheres.com/' + cerberus_img
        cerberus_hemisphere = {"Title": cerberus_title, "URL": cerberus_img_url}
        hemisphere_image_urls.append(cerberus_hemisphere)

    url5 = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url5)
    html = browser.html
    soup5 = bs(html, "html.parser")
    results5 = soup5.find_all('body', id ="results")

    for result in results5:
        schiaparelli_title = soup5.find('h2', class_='title').text
        downloads = soup5.find('div', class_ = 'downloads')
        li = downloads.find('li')
        schiaparelli_img = li.find('a')['href']
        schiaparelli_img_url = 'https://marshemispheres.com/' + schiaparelli_img
        schiaparelli_hemisphere = {"Title": schiaparelli_title, "URL": schiaparelli_img_url}
        hemisphere_image_urls.append(schiaparelli_hemisphere)

    url6 = "https://marshemispheres.com/syrtis.html"
    browser.visit(url6)
    html = browser.html
    soup6 = bs(html, "html.parser")
    results6 = soup6.find_all('body', id ="results")

    for result in results6:
        syrtis_major_title = soup6.find('h2', class_='title').text
        downloads = soup6.find('div', class_ = 'downloads')
        li = downloads.find('li')
        syrtis_major_img = li.find('a')['href']
        syrtis_major_img_url = 'https://marshemispheres.com/' + syrtis_major_img
        syrtis_major_hemisphere = {"Title": syrtis_major_title, "URL": syrtis_major_img_url}
        hemisphere_image_urls.append(syrtis_major_hemisphere)

    url7 = "https://marshemispheres.com/valles.html"
    browser.visit(url7)
    html = browser.html
    soup7 = bs(html, "html.parser")
    results7 = soup7.find_all('body', id ="results")

    for result in results7:
        valles_marineris_title = soup7.find('h2', class_='title').text
        downloads = soup7.find('div', class_ = 'downloads')
        li = downloads.find('li')
        valles_marineris_img = li.find('a')['href']
        valles_marineris_img_url = 'https://marshemispheres.com/' + valles_marineris_img
        valles_marineris_hemisphere = {"Title": valles_marineris_title, "URL": valles_marineris_img_url}
        hemisphere_image_urls.append(valles_marineris_hemisphere)

    
    mars_data = {"news_title": news_title,"news_p": news_p,
        "featured_image": featured_image_url, 
        "mars_table": mars_table, 
        "cerberus_title": cerberus_title, "cerberus_img_url": cerberus_img_url,
        "schiaparelli_title": schiaparelli_title, "schiaparelli_img_url": schiaparelli_img_url,
        "syrtis_major_title": syrtis_major_title, "syrtis_major_img_url": syrtis_major_img_url,
        "valles_marineris_title": valles_marineris_title, "valles_marineris_img_url": valles_marineris_img_url
    } 
    
    
    
    browser.quit()
    
    return mars_data
