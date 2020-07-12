from urllib.parse import unquote
import requests
import re
from lxml import etree
import pypinyin


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.173'
    }

s = requests.Session()

def login(laccount, lpassword):
    """ 根据账号（手机号）密码登录linkedin """
    
    r = s.get('https://www.linkedin.com/login', headers=headers)
    tree = etree.HTML(r.content)
    csrfToken = ''.join(tree.xpath('//*[@id="app__container"]/main/div[2]/form/input[1]/@value'))
    sIdString = ''.join(tree.xpath('//*[@id="app__container"]/main/div[2]/form/input[3]/@value'))
    pageInstance = ''.join(tree.xpath('//*[@id="app__container"]/main/div[2]/form/input[5]/@value'))
    loginCsrfParam = ''.join(tree.xpath('//*[@id="app__container"]/main/div[2]/form/input[9]/@value'))

    payload = {
        'csrfToken': csrfToken,
        'session_key': laccount,
        'ac': 0,
        'sIdString': sIdString,
        'parentPageKey': 'd_checkpoint_lg_consumerLogin',
        'pageInstance': pageInstance,
        'trk': '',
        'authUUID': '',
        'session_redirect': '',
        'loginCsrfParam': loginCsrfParam,
        'fp_data': 'default',
        'apfc': {},
        '_d': 'd',
        'showGoogleOneTapLogin': 'true',
        'controlId': 'd_checkpoint_lg_consumerLogin-login_submit_button',
        'session_password': lpassword
    }
    rs = s.post('https://www.linkedin.com/checkpoint/lg/login-submit', data=payload)
    return rs

def getName(url):  # 爬取用户名
    rs = s.get(url)
    rs.encoding = 'utf-8'
    content = unquote((rs.text).replace('&quot;', '"'))
    try:  # 正则匹配姓名
        firstname = re.findall('"multiLocaleFirstName":{"en_US":"(.*?)"}', content)[0]
        lastname = re.findall('"multiLocaleLastName":{"en_US":"(.*?)"}', content)[0]
    except:
        try:
            firstname = re.findall('"multiLocaleFirstName":{"[a-z]+_[A-Z]+":".*?","[a-z]+_[A-Z]+":"(.*?)"}', content)[0]
            lastname = re.findall('"multiLocaleLastName":{"[a-z]+_[A-Z]+":".*?","[a-z]+_[A-Z]+":"(.*?)"}', content)[0]
        except:
            firstname = re.findall('"multiLocaleFirstName":{"[a-z]+_[A-Z]+":"(.*?)"}', content)[0]
            lastname = re.findall('"multiLocaleLastName":{"[a-z]+_[A-Z]+":"(.*?)"}', content)[0]
                    
    firstname = pypinyin.slug(firstname,separator='')  # 中文转拼音
    lastname = pypinyin.slug(lastname,separator='')
    name = firstname + ' ' + lastname
    return name
   
def getNamewithoutLogin(url):   # 暂不可用
    rs = s.get(url,headers=headers)
    rs.encoding = 'utf-8'
    print(rs.text)
    tree = etree.HTML(rs.content)
    name = tree.xpath('/html/body/main/section[1]/section/section[1]/div/div[1]/div[1]/h1/text()')
    return name

if __name__ == '__main__':
    rs = login(laccount='your account', lpassword='your password')
    name = getName('https://www.linkedin.com/in/jennieohyoung/zh-cn')
    print(name)
