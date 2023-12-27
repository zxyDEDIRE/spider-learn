import re

from bs4 import BeautifulSoup
import requests
import lxml

class Demo:
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

    def tip(self):
        url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'
        html = self.get_html(url)

        soup = BeautifulSoup(html, 'html.parser')  # 执行速度适中 文档容错能力强
        soup = BeautifulSoup(html, "xml")  # 速度快 文档容错能力强
        soup = BeautifulSoup(html, "html5lib")  # 最好的容错性 以浏览器的方式解析文档 生成HTML5格式的文档
        soup = BeautifulSoup(html, 'lxml')  # 速度快 唯一支持XML的解析器

        # print(soup.prettify())  # 按照标准的缩进格式的结构输出:
        print(soup.title)  # <title>关于更新全国统计用区划代码和城乡划分代码的公告 </title>
        print(soup.title.string)  # 关于更新全国统计用区划代码和城乡划分代码的公告
        print(soup.title.parent.name)
        print(soup.map)
        print(soup.map['id'])
        print(soup.map['name'])
        # print(soup.find_all('tr'))
        print(soup.map.attrs)  # 直接取属性
        print(soup.map.contents)  # tag的 .contents 属性可以将tag的子节点以列表的方式输出:
        for i in soup.map.children:  # 通过tag的 .children 生成器,可以对tag的子节点进行循环:
            print(i)
        for i in soup.map.descendants:  # .descendants 属性可以对所有tag的子孙节点进行递归循环 [5] :
            print(i)
        for i in soup.map.strings:  # 如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取:
            print(i)
        # print(soup.map.parent)  # 通过 .parent 属性来获取某个元素的父节点
        print(soup.map.parent.name + '\n')
        for i in soup.map.parents:  # 通过元素的 .parents 属性可以递归得到元素的所有父辈节点
            if i is None:
                print(i)
            else:
                print(i.name)
        print('')
        for i in soup.map.next_siblings:  # 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点:
            print(i.name)
        for i in soup.map.previous_siblings:
            print(i.name)
        print(soup.map.next_element.name, soup.map.next_element)  # 下一个被解析的对象(字符串或tag),结果可能与 .next_sibling 相同,但通常是不一样的
        print(soup.map.previous_element.name, soup.map.previous_element)  # 它指向当前被解析的对象的前一个解析对象:
        # for i in soup.map.next_elements:  # 迭代器就可以向前或向后访问文档的解析内容,
        #     print(i)
        # print(soup.find_all(re.compile('^t')))  # 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.

    def main(self):
        url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find_all('tbody')[2].find_all('tbody')[0].find_all('tr', class_="provincetr")
        for i in data:
            for j in i.find_all('td'):
                j = j.a
                if j is None: continue
                p_name = j.get_text()
                href_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'+j.get('href')
                soup_c = BeautifulSoup(self.get_html(href_url),'lxml').find_all('tr',class_="citytr")
                for it in soup_c:
                    print(p_name+'-'+it.find_all('a')[1].get_text())



if __name__ == '__main__':
    # Demo().tip()
    Demo().main()
