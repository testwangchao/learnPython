# coding:utf-8
import re
from collections import Counter
from userTable import user_table

def demo(test_data, key_data, delimiter='.'):
    for key in key_data.split(delimiter):
        if isinstance(test_data, dict):
            test_data = test_data.get(key)
        elif isinstance(test_data, list):
            return test_data[int(key)]
    return test_data


def arg_demo(text):
    text = text.replace('\\', "")
    text = text.replace("null", "None")
    text = re.sub('''"history_select":"{.*?}}}",''', "", text)
    text = eval(text)
    return text


def return_card(card):
    card_type = {"A": u"黑桃", "B": u"红桃", "C": u"梅花", "D": u"方块"}
    type = re.match("(\w)(\d+)", card, re.I).group(1)
    number = re.match("(\w)(\d+)", card, re.I).group(2)
    all_data = []
    # if int(number) == 1:
    #     number = 'A'
    # elif int(number) == 11:
    #     number = 'J'
    # elif int(number) == 12:
    #     number = 'Q'
    # elif int(number) == 13:
    #     number = 'K'
    all_data.append(int(number))
    if type in card_type.keys():
        all_data.append(card_type.get(type))
    return all_data


def get_type(card):
    # 所有的牌
    all_pai = []
    for i in card:
        all_pai.extend(return_card(i.get("card")))
    # print all_pai
    if len(set(all_pai[0::2])) == 1:
        print u"豹子{0}".format(list(set(all_pai[0::2]))[0])
    elif len(set(all_pai[0::2])) == 2:
        # print all_pai[0::2]
        for card_value, time in Counter(all_pai[0::2]).items():
            if Counter(all_pai[0::2]).get(card_value) == 2:
                print u"对子{0}".format(card_value)
    elif len(set(all_pai[1::2])) == 1:
        sort_card_value = all_pai[0::2]
        sort_card_value.sort(reverse=False)
        if sort_card_value == [1, 12, 13]:
            print u"同花顺QKA"
        elif sort_card_value[0] + 1 == sort_card_value[1] and sort_card_value[0] + 2 == sort_card_value[2]:
            print u"同花顺{0}".format(" ".join([str(i) for i in sort_card_value]))
        else:
            print u"同花{0}".format(" ".join([str(i) for i in sort_card_value]))
    else:
        # print "".join(all_pai[0::2])
        sort_card_value = all_pai[0::2]
        sort_card_value.sort(reverse=False)
        if sort_card_value == [1, 12, 13]:
            print u"顺子QKA"
        elif sort_card_value[0] + 1 == sort_card_value[1] and sort_card_value[0] + 2 == sort_card_value[2]:
            print u"顺子{0}".format(" ".join([str(i) for i in sort_card_value]))
        else:
            print u"高牌{0}".format(" ".join([str(i) for i in sort_card_value]))


def main(text):
    data = arg_demo(text)
    user_data = demo(data, "msg.user")
    id = demo(user_data, "id")
    card_list = demo(user_data, "card")
    if id in user_table.keys():
        print user_table.get(id)
    else:
        print id
    get_type(card_list)
    print "\t"


if __name__ == '__main__':
    # text1 = '''{"msg":{"user":{"id":"1011462","user_login":"test1011462","mobile":null,"password":"qinglong","is_grade":"0","fk":"0","gailv":"0","create_time":"2018-03-21 09:23:11","last_time":"2018-03-21 14:35:05","status":"0","disable_notice":null,"last_login_ip":"117.136.38.134","reg_ip":"106.38.120.114","money":"0","img":"http:\/\/thirdwx.qlogo.cn\/mmopen\/vi_32\/Q0j4TwGTfTLV9rhlIrTlre0XHIA7ylPb550FuicJ61yWeEUHc3L2XA04UDnjf0J3v6T5QibhJo0kiab9SFnUibvpJA\/132","nickname":"546L6LaF8J+Pgw==","nickname_base64":"546L6LaF8J+Pgw==","token":"c458e91e5ad0d11d916d6f5550e8483d","level":"0","sfgl":"0","openid":"oKAqu08shQyjq6XPRXL40ZFBrPbM","daycard":"0","sex":"1","hyid":"0","history_select":"{\"16\":{\"id\":\"33\",\"rule\":{\"js\":0,\"cm\":0,\"sx\":0}}}","online":1,"zt":1,"room":47616,"card":[{"val":11,"card":"A13","pai":"13","hs":3,"zt":"1","dx":47},{"val":9,"card":"D11","pai":"11","hs":0,"zt":"1","dx":36},{"val":8,"card":"D10","pai":"10","hs":0,"zt":"1","dx":32}],"cardmax":"022201947","typexx":0,"index":0,"dqjf":-8,"djjf":-4,"tpzt":0,"beishu":null,"qbank":null,"niu":null}},"act":"adduser"}'''
    with open("C:\\Users\\Administrator\\Desktop\\new3.txt", 'r') as file:
        for i in re.findall('''({"msg":{"user".*?"dx":\d+}],)''', file.read()):
            main(i + "}}}")
