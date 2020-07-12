def generateName(name):  # 根据名字生成可能的邮箱用户名前缀

    emailName1 = name.strip().replace(' ','').lower()
    emailName2 = name.strip().replace(' ','.').lower()
    emailName3 = name.strip().replace(' ','_').lower()
    emailName4 = name.strip().replace(' ','-').lower()

    nameList = name.strip().split(' ')

    try :
        emailName5 = (nameList[1] + nameList[0]).lower()
        emailName6 = (nameList[1] + '.' + nameList[0]).lower()
        emailName7 = (nameList[1] + '_' + nameList[0]).lower()
        emailName8 = (nameList[1] + '-' + nameList[0]).lower()

        emailName9 = nameList[0].lower()
        emailName10 = nameList[1].lower()

        emailName11 = (nameList[1] + nameList[0][0]).lower()
        emailName12 = (nameList[1] + '.' + nameList[0][0]).lower()
        emailName13 = (nameList[1] + '_' + nameList[0][0]).lower()
        emailName14 = (nameList[1] + '-' + nameList[0][0]).lower()

        emailName15 = (nameList[0] + nameList[1][0]).lower()
        emailName16 = (nameList[0] + '.' + nameList[1][0]).lower()
        emailName17 = (nameList[0] + '_' + nameList[1][0]).lower()
        emailName18 = (nameList[0] + '-' + nameList[1][0]).lower()

        emailName19 = (nameList[1][0] + nameList[0]).lower()
        emailName20 = (nameList[1][0] + '.' + nameList[0]).lower()
        emailName21 = (nameList[1][0] + '_' + nameList[0]).lower()
        emailName22 = (nameList[1][0] + '-' + nameList[0]).lower()

        emailName23 = (nameList[0][0] + nameList[1]).lower()
        emailName24 = (nameList[0][0] + '.' + nameList[1]).lower()
        emailName25 = (nameList[0][0] + '_' + nameList[1]).lower()
        emailName26 = (nameList[0][0] + '-' + nameList[1]).lower()

        emailName27 = (emailName2[0][0]+emailName2[1][0]).lower()
        emailName28 = (emailName2[1][0]+emailName2[0][0]).lower()
        
        for i in range(1,29):    
            yield locals()['emailName'+str(i)]    
    
    except :
        yield emailName1

if __name__ == "__main__":
    for name in generateName(' Edward '):
        print(name)


