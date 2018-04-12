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

def return_pai():
    pass

def main(text):
    data = arg_demo(text)
    user_data = demo(data,"msg.user")
    id = demo(user_data,"id")
    card_list = demo(user_data,"card")
    print id
    card_data = []
    for card in card_list:
        print "".join(return_card(card.get("card")))
        # card_data.append(return_card(card.get("card")))
    # print card_data[0]
if __name__ == '__main__':
    with open("C:\\Users\\wangchao88\\Desktop\\pai1.txt",'r') as file:
        for i in re.findall('''({"msg":{"user".*?"dx":\d+}],)''',file.read()):
            main(i+"}}}")