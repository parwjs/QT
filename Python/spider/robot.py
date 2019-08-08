import urllib.request
# import urllib.parse
import json,re

def contract(message):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType":"0",
        "perception":{
            "inputText":{
                "text":message,
            },
            "selfInfo":{
                    "location": {
                    "city": "大庆",
                    "province": "黑龙江",
                    "street": "龙凤区"
            }

        }
    },
        "userInfo":{
            "apiKey":"201de2db93a24714b61224a3ddd29b4d",
            "userId":"439189"
        }
    }

    # postdata = urllib.parse.urlencode(data).encode('utf-8')
    postdata = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url,postdata)
    datas = urllib.request.urlopen(req).read().decode('utf-8','ignore')
    reg = '\{"text":"(.*?)"'
    # print(datas["results"][0]["values"]["text"])
    text = re.compile(reg,re.S).findall(datas)
    print(text)

if __name__ == '__main__':
    while True:
        # code = input("请输入消息类型:").strip()
        message = input("请输入信息:").strip()
        if message == "1":
            break
        # contract(code,message)
        contract(message)