import requests
from bs4 import BeautifulSoup
from lxml import etree

def getLink(companyName):
    
    number = 1
    s = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.173'
        }

    pre_url = 'https://cn.bing.com'
    rs = s.get(pre_url,headers=headers)
    
    for i in range(1,51):  # 爬取50页
        url = 'https://cn.bing.com/search?q=site%3alinkedin.com%2fin+{}&first={}&FORM=PORE'.format(companyName,number)
        rs = s.get(url,headers=headers)

        soup = BeautifulSoup(rs.content,'html.parser')

        link_list = soup.find_all('li',class_='b_algo')

        for item in link_list:
            html = etree.HTML(str(item))
            link = html.xpath('//*/h2/a/@href')
            yield link[0]
        number = len(link_list) * i + 1

if __name__ == "__main__":
    for item in getLink('github'):  
        print(item)