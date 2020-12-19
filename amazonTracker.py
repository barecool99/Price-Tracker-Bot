import requests
from bs4 import BeautifulSoup
import smtplib #this sends email

URL = "https://www.amazon.co.uk/Soundcore-Microphones-Reduction-Waterproof-Earphones-Black/dp/B07SJR6HL3/ref=sr_1_10?dchild=1&keywords=earphones&psr=EY17&qid=1606683146&s=black-friday&sr=1-10"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
PRICE_VALUE = 35
EMAIL_ADDRESS = "ENTER YOUR EMAIL HERE"
 #if amazon price is less than our desired price (PRICE_VALUE) than send us an email
def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still £{diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        sendEmail()
    pass
#this gets the price and text name 
def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_dealprice').get_text().strip()[1:4]
    print(title)
    print(price)
    return price
#this function sends an email
def sendEmail():
    subject = "Saugat Python Script:Amazon Price for earbuds Dropped!"
    mailtext='Subject:'+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'ENTER YOUR EMAIL PASS HERE!')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    print("Sent Email!")
    pass

if __name__ == "__main__":
    trackPrices()
