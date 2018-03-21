# coding:utf-8
import re

def demo(test_data, key_data,delimiter='.'):
    for key in key_data.split(delimiter):
        if isinstance(test_data, dict):
            test_data = test_data.get(key)
        elif isinstance(test_data, list):
            return test_data[int(key)]
    return test_data

def arg_demo(text):
    text = text.replace('\\',"")
    text = text.replace("null","None")
    text = re.sub('''"history_select":"{.*?}}}",''',"",text)
    text = eval(text)
    return text


def return_card(card):
    card_type = {"A": u"黑桃", "B": u"红桃", "C":u"梅花", "D": u"方块"}
    type = re.match("(\w)(\d+)",card,re.I).group(1)
    number = re.match("(\w)(\d+)",card,re.I).group(2)
    if int(number) == 1:
        number = 'A'
    elif int(number) == 11:
        number='J'
    elif int(number) == 12:
        number='Q'
    elif int(number) == 13:
        number='K'
    if type in card_type.keys():
        return card_type.get(type)+number


def main(text):
    data = arg_demo(text)
    user_data = demo(data,"msg.user")
    id = demo(user_data,"id")
    card_list = demo(user_data,"card")
    print id
    for card in card_list:
        print "".join(return_card(card.get("card")))


if __name__ == '__main__':
    # text1 = '''{"msg":{"user":{"id":"1011462","user_login":"test1011462","mobile":null,"password":"qinglong","is_grade":"0","fk":"0","gailv":"0","create_time":"2018-03-21 09:23:11","last_time":"2018-03-21 14:35:05","status":"0","disable_notice":null,"last_login_ip":"117.136.38.134","reg_ip":"106.38.120.114","money":"0","img":"http:\/\/thirdwx.qlogo.cn\/mmopen\/vi_32\/Q0j4TwGTfTLV9rhlIrTlre0XHIA7ylPb550FuicJ61yWeEUHc3L2XA04UDnjf0J3v6T5QibhJo0kiab9SFnUibvpJA\/132","nickname":"546L6LaF8J+Pgw==","nickname_base64":"546L6LaF8J+Pgw==","token":"c458e91e5ad0d11d916d6f5550e8483d","level":"0","sfgl":"0","openid":"oKAqu08shQyjq6XPRXL40ZFBrPbM","daycard":"0","sex":"1","hyid":"0","history_select":"{\"16\":{\"id\":\"33\",\"rule\":{\"js\":0,\"cm\":0,\"sx\":0}}}","online":1,"zt":1,"room":47616,"card":[{"val":11,"card":"A13","pai":"13","hs":3,"zt":"1","dx":47},{"val":9,"card":"D11","pai":"11","hs":0,"zt":"1","dx":36},{"val":8,"card":"D10","pai":"10","hs":0,"zt":"1","dx":32}],"cardmax":"022201947","typexx":0,"index":0,"dqjf":-8,"djjf":-4,"tpzt":0,"beishu":null,"qbank":null,"niu":null}},"act":"adduser"}'''
    # text2 = ''''''
    # text3 = ''''''
    # text4 = ''''''
    # text5 = ''''''
    # text6 = ''''''
    # text7 = ''''''
    # text8 = ''''''
    # text9 = ''''''
    # all = [text1,text2,text3,text4,text5,text6,text7,text8,text9]
    # for i in all:
    #     main(i)
    with open("C:\\Users\\Administrator\\Desktop\\new3.txt",'r') as file:
        for i in re.findall('''({"msg":{"user".*?"dx":\d+}],)''',file.read()):
            main(i+"}}}")
