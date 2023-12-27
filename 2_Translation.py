import requests
import json


def main(str):
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"
    }
    data = {
        "i": str,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16683938470443",
        "sign": "c3a09365e7e742ec6df3f58279cd6576",
        "lts": "1668393847044",
        "bv": "37dd3c60883fcf3fdfbbfa8fa2c4565d",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    r = requests.post(url=url, data=data, headers=headers)
    res = r.json()
    print(res)
    # print(res['translateResult'][0][0]['tgt'])

if __name__ == "__main__":
    str=input()
    # print(str)
    # str.replace('\n','')
    # print("\n")
    # print(str)
    main(str)