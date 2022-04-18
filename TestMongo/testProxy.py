import re

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
}

"""
    python博客：https://cuiqingcai.com/7048.html
"""
def get_html(url, headers=headers, encoding="UTF-8"):
    decode = requests.get(url, headers=headers).content.decode(encoding=encoding)
    # print(decode)
    return etree.HTML(decode)


proxyAddr = set({})


def isIPAddr(value):
    return re.match(
        r"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d):\d+",
        value)


# 快代理
def kuaiProxy():
    for pageNum in range(int(
            get_html('https://www.kuaidaili.com/free/inha/1/').xpath('//*[@id="listnav"]/ul/li[last()-1]/a/text()')[
                0])):
        content = get_html('https://www.kuaidaili.com/free/inha/%s/' % pageNum)
        for el in content.xpath('//*[@id="list"]/table/tbody/tr'):
            ip = el.xpath('./td[1]/text()')[0]
            port = el.xpath('./td[2]/text()')[0]
            print(ip, port)
            proxyAddr.add(ip + ":" + port)


# 西刺代理
def xicidaili():
    content = get_html('https://www.xicidaili.com')
    for el in content.xpath('//tr'):
        if el.xpath("string-length(./td/text()) > 0"):
            print(el.xpath("string(concat(./td[2]/text(),':',./td[3]/text()))"))
            proxyAddr.add(el.xpath("string(concat(./td[2]/text(),':',./td[3]/text()))"))


def cnproxy():
    content = get_html('https://cn-proxy.com/')
    for el in content.xpath('//tr'):
        if el.xpath("string-length(./td/text()) > 0") and isIPAddr(
                el.xpath("string(concat(./td[1]/text(),':',./td[2]/text()))")):
            print(el.xpath("string(concat(./td[1]/text(),':',./td[2]/text()))"))
            proxyAddr.add(el.xpath("string(concat(./td[1]/text(),':',./td[2]/text()))"))
def xiladaili():
    content = get_html('http://www.xiladaili.com/')
    for el in content.xpath('//tr/td[1]'):
        if el.xpath("string-length(./text()) > 0") and isIPAddr(el.xpath("string(./text())")):
            proxyAddr.add(el.xpath("string(./text())"))


def goubanjia():
    content = get_html('http://www.goubanjia.com/')
    for el in content.xpath('//*[@id="services"]/div/div[2]/div/div/div/table/tbody/tr'):
        ip = []
        len2 = int(el.xpath('count(./td[1]/*)'))
        i = 0
        for td in el.xpath('./td[1]/*'):
            style_attr = td.xpath('./@style')
            if len(style_attr) == 0 or (
                    len(style_attr) > 0 and re.match(r'display:\s*inline-block\s*(;)?', style_attr[0]) != None):
                if len(td.xpath('./text()')) > 0:
                    if len2 - 1 == i:
                        ip.append(':')
                    ip.append(td.xpath('./text()')[0].strip())
            i += 1
        proxyAddr.add(''.join(ip))


if __name__ == '__main__':
    # kuaiProxy()
    # for x in range(100):
    goubanjia()
    # xicidaili()
    # cnproxy()
    # xiladaili()
    print(len(proxyAddr))
