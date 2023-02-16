import bs4 as bs
import requests
import lxml.etree
import lxml.html
from .models import Product
# from celery import shared_task
# For jobs 

# Xpath constants for flipkart
name_path = '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span//text()'
sale_price_path = '//div[contains(text(),"₹")]//text()'
price_path ='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[2]//text()'
image_path = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/img/@src'
description_path = '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[9]/div[3]/div/div[2]/div[1]//text()'
category_path = '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/div[2]//text()'

def cleanText(text):
    if type(text) == int:
        return text
    text = text.replace('\n', '').replace('\r', '').replace('\t', '').replace('', '').replace('₹', '').replace(',', '')
    return 0 if text== "" else int(text)

def scrapData(url):
    print("scrapper running....")
    # Get the html content of the url
    r = requests.get(url)
    soup = lxml.html.fromstring(r.content)
    name = soup.xpath(name_path)[0] if len(soup.xpath(name_path))  else ""
    sale_price = soup.xpath(sale_price_path)[0] if len(soup.xpath(sale_price_path))  else 0
    price = soup.xpath(price_path)[0] if len(soup.xpath(price_path))  else 0
    image = soup.xpath(image_path)[0] if len(soup.xpath(image_path))  else ""
    description = soup.xpath(description_path)[0] if len(soup.xpath(description_path))  else ""
    category = soup.xpath(category_path)[0]  if len(soup.xpath(category_path))  else ""
    print(
      {
        "name": name,
        "sale_price": cleanText(sale_price),
        "price": cleanText(sale_price),
        "image": image,
        "description": description,
        "category": category
      }
    )
    product = Product.objects.create(title=name, price= cleanText(sale_price) ,
     discount_price= cleanText(sale_price) , category='Mobile', description=description, image=image, link=url)
    return product

# scrapData('https://www.flipkart.com/sony-alpha-full-frame-ilce-7m2k-bq-in5-mirrorless-camera-body-28-70-mm-lens/p/itm92df94dc68fff?pid=DLLF6QZPNKTQMS8J&lid=LSTDLLF6QZPNKTQMS8JPI2J50&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_2&otracker=hp_omu_Best%2Bof%2BElectronics_1_3.dealCard.OMU_Q5LU1U8PHMK6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_1_NA_view-all_3&fm=neo%2Fmerchandising&iid=0e7c39cb-2aea-4817-8b4d-70dfe1cbe33d.DLLF6QZPNKTQMS8J.SEARCH&ppt=hp&ppn=homepage&ssid=pku527m4o00000001676548517363')