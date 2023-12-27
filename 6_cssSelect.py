import requests
from lxml import html
import cssselect

etree = html.etree


class test:  # css 选择器
    def to_string(self, html):
        return etree.tostring(html, encoding='utf-8').decode('utf-8')

    def main(self):
        text = '''
                     <div class="item-1" style="color:red;"><a href="link1.html">Python知识</a></div>
                     <div class="item-2"><a href="link2.html"><div>学习Python</div></a></div>
                     <div class="item-3 item-4"><a href="link5.html">很好玩</div>
                '''
        html = etree.HTML(text)
        result = html.cssselect('div.item-1.item-2 a')
        # 选择div标签并且含有class属性 且值含有 'item-1'与 'item-2' 下的a 标签子节点
        for i in result:
            print(i.text)
            print(i.get('herf'))


class test_1:
    def get_html(self, url):
        try:
            head = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
            }
            r = requests.get(url=url, headers=head)
            r.raise_for_status()
            # r.encoding = 'utf-8'
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return "错误"

    def tostring(self, a):
        return etree.tostring(a, encoding='utf-8').decode('utf-8')

    def main(self):
        text = '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        .intro
        {
        background-color:yellow;
        }
        </style>
        </head>

        <body>
        <h1>欢迎来到我到的主页</h1>

        <div class="intro">
        <p>我是唐老鸭。</p>
        <p>我住在 Duckburg。</p>
        </div>

        <p>我最好的朋友是米老鼠。</p>

        </body>
        </html>
        '''
        html = etree.HTML(text)
        print(self.tostring(html))
        print('------------------分隔符---------------')
        result = html.cssselect('div.intro')
        for i in result:
            print(self.tostring(i))
        print(type(result))

    def doit(self):
        url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'
        html_text = self.get_html(url)
        html = etree.HTML(html_text)
        result = html.cssselect('table.provincetable tr.provincetr a')
        for i in result:
            p_name = i.text
            new_url = url + i.get('href')
            new_html_text = self.get_html(new_url)
            new_html = etree.HTML(new_html_text)
            data = new_html.cssselect('tr.citytr a')
            for j in range(1, len(data), 2):
                print(p_name, data[j].text)


if __name__ == '__main__':
    # test_1().main()
    test_1().doit()
