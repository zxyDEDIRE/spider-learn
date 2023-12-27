import requests
from bs4 import BeautifulSoup
from lxml import html
etree = html.etree
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
def main():
    url = 'https://www.tianqishi.com/changsha/20220506.html'
    html_text = getHtml(url)
    soup = BeautifulSoup(html_text, 'lxml')
    res = soup.find_all('div',class_='weather_fifteen_l-1 weilai24')[0].find_all('table')[1]
    for i in res:
        li = i.get_text()
        if len(li)==1:continue

        ans = li.split('\n')
        print(ans)
if __name__ == '__main__':
    main()