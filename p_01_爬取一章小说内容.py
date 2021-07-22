import re
from bs4 import BeautifulSoup  # 必须要导入 bs4 库
import requests

"""
【代码待完成……】
参考资料见：
1、https://blog.csdn.net/z1360408752/article/details/111781203?utm_source=app&app_version=4.11.0&code=app_1562916241&uLinkId=usr1mkqgl919blen
2、https://blog.csdn.net/weixin_40962422/article/details/78729132?utm_source=app&app_version=4.11.0&code=app_1562916241&uLinkId=usr1mkqgl919blen
3、【BeautifulSoup库】https://blog.csdn.net/slhlde/article/details/81937838?utm_source=app&app_version=4.11.0&code=app_1562916241&uLinkId=usr1mkqgl919blen
"""

# header 用来伪装浏览器发送请求
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'}
if __name__ == "__main__":
    url = 'http://www.biqikan.com/54/54638/23852196.html'

    req = requests.get(url, headers=header)  # 向目标网站发送 get 请求
    req.encoding = 'gbk'  # 防止乱码
    html = req.text
    div_bf = BeautifulSoup(html, 'html.parser')  # 创建对象，解析 html 信息

    # print(div_bf.prettify())  # 格式化输出
    """ [<div class="contentbox" id="htmllContent"> """
    section_text = div_bf.select('.chapter_read .abstract #htmllContent')  # 按照父子关系细细划分
    # [0].text



    # print(div_bf.select('.contentbox'))  # 通过类名查找
    # texts = div_bf.select('#htmllContent')  # 通过 id 名定位查找
    print(section_text)
    s = str(section_text)
    with open('第1章 头条影后（1）.txt', 'w', encoding='utf-8') as f:
        f.write(s)


print('task over ！')


    # title_re = re.compile(r'<li class="active">(.*?)</li>')  # 取出文章标题
    # text_re = re.compile(r'<br><br>([\s\S]*?)</div>')  # 由于正文部分有很多的换行符，故使用 [\s\S]
    # title = re.findall(title_re, result)  # 找出标题
    # text = re.findall(text_re, result)  # 找出正文
    # title = title[0]  # 由于返回的 title 是列表，故取出列表的第一项
    # print(title)  # 打印出标题





