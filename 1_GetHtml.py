import requests
import xlrd


def getHtml(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
        }
        r = requests.get(url=url, headers=headers)  # 不带参数的get请求
        r.raise_for_status()  # 判断返回的Response类型状态是不是200
        r.encoding = 'utf-8'  # 重新编码utf-8
        r.encoding = r.apparent_encoding  # 从内容中分析出的响应内容编码方式（备选编码方式）
        return r.text  # HTTP响应内容的字符串形式
    except:
        return "错误"


if __name__ == "__main__":
    print("ES")
    url = "https://api.ixiaowai.cn/api/api.php"
    SavePath = "C:\\Users\\tob\\Desktop\\test\\chong\\"
    try:
        for i in range(1, 20):
            r = requests.get(url)
            with open(SavePath + str(i) + ".jpg", "wb+") as file:  # wb+是以二进制方式进行读写
                file.write(r.content)
            print(i)
    except:
        print("ERROR")
