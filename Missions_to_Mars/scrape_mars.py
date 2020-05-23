#!/usr/bin/env python
# coding: utf-8


# Dependencies
from bs4 import BeautifulSoup
import urllib.request
from splinter import Browser
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    article_data = {} 
    urls = ['https://mars.nasa.gov/news/', 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars', 'https://twitter.com/marswxreport?lang=en', 
    'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced', 
    'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
    'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced']
    browser.visit(urls[0])



# Parse HTML with Beautiful Soup

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
# Retrieve all elements that contain book information
    article_data["news_title"] = soup.find("h3").get_text()
    article_data["news_desc"] = soup.find("div", class_="article_teaser_body").get_text()


    # Close the browser after scraping
    browser.quit()


# URL of page to be scraped
    browser = init_browser()

    browser.visit(urls[1])



# HTML object
    html = browser.html
# Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all elements that contain book information

    featuredMars = soup.find('article', class_='carousel_item')
    featuredMarsImg = featuredMars['style']
    featuredMarsImgslice = featuredMarsImg.split()
    marsImg = featuredMarsImgslice[1].split("'")
    featured_image_url = 'https://www.jpl.nasa.gov/' + marsImg[1]

    browser.quit()

    browser = init_browser()

    browser.visit(urls[2])



# HTML object
    html = browser.html
# Parse HTML with Beautiful Soup 
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find('article').text

    browser.quit()


    browser = init_browser()


    valles_data = {} 

# URL of page to be scraped
    browser.visit(urls[3])


# HTML object
    html = browser.html
# Parse HTML with Beautiful Soup 
    soup = BeautifulSoup(html, 'html.parser')
    valles_data['valles_title'] = soup.find('h2', class_='title').get_text()
    valles_img = soup.find('img', 'wide-image')
    valles_data['valles_img_url'] = valles_img['src']

    browser.quit()


    browser = init_browser()

    cerbeus_data = {}
# URL of page to be scraped
    browser.visit(urls[4])



# HTML object
    html = browser.html
# Parse HTML with Beautiful Soup 
    soup = BeautifulSoup(html, 'html.parser')
    cerbeus_data['cerbeus_title'] = soup.find('h2', class_='title').get_text()
    cerbeus_img = soup.find('img', 'wide-image')
    cerbeus_data['cerbeus_img_url'] = cerbeus_img['src']

    browser.quit()


    browser = init_browser()

    schiaparelli_data = {}
# URL of page to be scraped
    browser.visit(urls[5])



# HTML object
    html = browser.html
# Parse HTML with Beautiful Soup 
    soup = BeautifulSoup(html, 'html.parser')
    schiaparelli_data['schiaparelli_title'] = soup.find('h2', class_='title').get_text()
    schiaparelli_img = soup.find('img', 'wide-image')
    schiaparelli_data['schiaparelli_img_url'] = schiaparelli_img['src']

    browser.quit()


    browser = init_browser()

    syrtis_data = {}
# URL of page to be scraped
    browser.visit(urls[6])

# HTML object
    html = browser.html
# Parse HTML with Beautiful Soup 
    soup = BeautifulSoup(html, 'html.parser')
    syrtis_data['syrtis_title'] = soup.find('h2', class_='title').get_text()
    syrtis_img = soup.find('img', 'wide-image')
    syrtis_data['syrtis_img_url'] = syrtis_img['src']

    browser.quit()


    astro_url = 'https://astrogeology.usgs.gov'
    hemisphere_image_urls = [
        {"title": valles_data['valles_title'], "img_url": astro_url + valles_data['valles_image_url']},
        {"title": cerbeus_data['cerbeus_title'], "img_url": astro_url + cerbeus_data['cerbeus_img_url']},
        {"title": schiaparelli_data['schiaparelli_title'], "img_url": astro_url + schiaparelli_data['schiaparelli_img_url']},
        {"title": syrtis_data['syrtis_title'], "img_url": astro_url + syrtis_data['syrtis_img_url']},
    ]
    return article_data, featured_image_url, mars_weather, valles_data, cerbeus_data, schiaparelli_data, hemisphere_image_urls, syrtis_data
