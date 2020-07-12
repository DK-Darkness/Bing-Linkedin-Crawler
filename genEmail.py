"""
输入公司域名获取其员工的邮箱地址
"""
from utils import *

def generateEmail(companyName):
    for link in getLink(companyName.split('.')[0]):
        print(link)
        name = getName(link)
        for usrname in generateName(name):
            email = usrname + '@' + companyName
            yield email

if __name__ == "__main__":
    for email in generateEmail('github.com'):
        print(email)

