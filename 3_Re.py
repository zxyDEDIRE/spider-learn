import requests
import re


class Demo():
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

    def matching(self, html):
        patten = re.compile(r'.*?html\'>(.*?)<br/></a>', re.S)
        return re.findall(patten, html)

    def matching_url(self, html):
        patten = re.compile(r'<td><a href=\'(.*?)\'>', re.S)
        ans = re.findall(patten, html)
        li = list()
        for i in ans:
            li.append('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/' + i)
        return li

    def h(self, url, ans):
        html = self.get_html(url)
        patten = re.compile(r'html\'>.*?html\'>(.*?)</a></td></tr>', re.S)
        data = re.findall(patten, html)
        for i in data:
            ans.append(i)
        return ans

    def f(self, url):
        html = self.get_html(url)
        data = self.matching(html)
        url_data = self.matching_url(html)
        for i in url_data:
            data = self.h(i, data)
        for i in data:
            print(i)

    def main(self):
        self.f('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/')


if __name__ == '__main__':
    Demo().main()
