import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/gp/product/B07X2KLYSF?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=RZ1F9R9ATRJP5PVNPGPJ'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


def check_price():


    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price1 = float(price[2:4])
    converted_price2 = float(price[5:8])
    converted_price = converted_price1*1000+converted_price2

    if (converted_price < 14999.0):
        send_mail()
    print(converted_price)
    print(title.strip())

    if (converted_price < 14999.0):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('abhip7th@gmail.com', 'sffipyulfwkfqbzl')
    subject ='Price Fell Down!'
    body = 'https://www.amazon.in/gp/product/B07X2KLYSF?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=RZ1F9R9ATRJP5PVNPGPJ'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'abhip7th@gmail.com',
        'abhip1st@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60*24*7*4)