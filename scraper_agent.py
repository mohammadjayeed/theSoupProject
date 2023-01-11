import mail_system
import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import date

urls = ["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch"]
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}


today = str(date.today()) + ".csv"
csv_file = open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['stock name','current price','previous close','open','bid','ask','days range','52 week range','volume','avg. volume'])

for url in urls:
    list_ = []
    target_page = requests.get(url,headers=headers)
    soup= BeautifulSoup(target_page.content, 'lxml')

    # print(target_page.content)

    header_info = soup.find_all('div',id='quote-header-info')[0]
    title = header_info.find('h1').get_text()
    list_.append(title)
    # print(header_info)
    price = header_info.find('div',class_='My(6px) Pos(r) smartphone_Mt(6px) W(100%)').find('fin-streamer').get_text()
    # print(price)
    list_.append(price)


    table_info = soup.find_all('div',class_ = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all('tr')

    for i in range(0,8):
        subject = table_info[i].find_all('td')[0].get_text()
        value = table_info[i].find_all('td')[1].get_text()
        # print(subject + " " + value)
        list_.append(value)
    csv_writer.writerow(list_)
    time.sleep(4)
csv_file.close()
mail_system.send(filename=today)