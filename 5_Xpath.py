import requests
from lxml import html
etree = html.etree


def a_Element():
    root = etree.Element('root')  # Element类
    print(root.tag)
    child = etree.SubElement(root, 'child')  # 添加一个子节点
    child.set('id', 'test_id')
    print(etree.tostring(root))


def b_tostring():
    root = etree.XML('<html><head/><body><p>Hello<br/>Python</p></body></html>')
    print(etree.tostring(root, method='xml'))  # 默认值为：xml
    print(etree.tostring(root, method='html'))  # 转成html


def c_XML_HTML():
    root = etree.XML("<root>data</root>")  # 将字符串转换成XML对象
    etree.tostring(root)
    print(etree.tostring(root))

    root = etree.HTML("<p>data</p>")  # 将字符串转换成HTML对象
    etree.tostring(root)
    print(etree.tostring(root))


def d_Xpath():
    text = "<div><h1>Python</h1></div>"
    html = etree.HTML(text)
    result = html.xpath('//*')
    for i in result:
        print(etree.tostring(i, encoding='utf-8').decode('utf-8'))


class Demo:  # xpath 语法
    def to_string(self, html):
        return etree.tostring(html, encoding='utf-8').decode('utf-8')

    def main(self):
        text = '''
             <div class="item-1" style="color:red;"><a href="link1.html">Python知识</a></div>
             <div class="item-2"><a href="link2.html"><div>学习Python</div></a></div>
             <div class="item-3 item-4"><a href="link5.html">很好玩</div>
        '''
        html = etree.HTML(text)  # 初始化生成Xpath对象 会补全html
        print(self.to_string(html))
        print('------------------分隔符---------------')
        print('print(html.xpath(\'/div\'))', html.xpath('/div'))  # 开头为html所以招不到div
        print('print(html.xpath(\'/html/body/div\'))')
        result = html.xpath('/html/body/div')
        #  找到html标签下的body 再从body找到div标签
        for i in result:
            print(self.to_string(i))
        print('------------------分隔符---------------')
        result = html.xpath('/html//div')  # 找到html标签下的所有div标签
        for i in result:
            print(self.to_string(i))
        print('------------------分隔符---------------')
        result = html.xpath('./body')  # 找到根节点下的body标签
        for i in result:
            print(self.to_string(i))
        print('------------------分隔符---------------')
        result = html.xpath('//a/../@class')  # a标签的父亲节点的class属性
        print(result)
        print('------------------分隔符---------------')
        result = html.xpath('//*')  # 选取文档中的所有标签
        for i in result:
            print(self.to_string(i))
        print('------------------分隔符---------------')
        result = html.xpath('//div[@class=\'item-2\']')  # 文档中的class属性为item-2的所有div标签
        for i in result:
            print(self.to_string(i))


class Test:
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

    def main(self):
        url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'
        html_text = self.get_html(url)
        html = etree.HTML(html_text)
        cnt = 1
        for i in range(4, 5):
            result_1 = html.xpath('/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tr[' + str(i) + ']//a/@href')
            result_2 = html.xpath('/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tr[' + str(i) + ']//text()')
            for j in range(0, len(result_1)):
                p_name = result_2[j]
                new_url = url + result_1[j]
                new_html_text = self.get_html(new_url)
                new_html = etree.HTML(new_html_text)
                path_1 = new_html.xpath('//table[@class=\'citytable\']//tr/td//text()')
                for k in range(1, len(path_1), 2):
                    print(p_name, path_1[k])


if __name__ == '__main__':
    # Demo().main()
    Test().main()
    input('Press <Enter>')

