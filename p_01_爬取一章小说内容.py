import re

import requests

"""
参考资料见：
1、https://blog.csdn.net/z1360408752/article/details/111781203?utm_source=app&app_version=4.11.0&code=app_1562916241&uLinkId=usr1mkqgl919blen
2、https://blog.csdn.net/weixin_40962422/article/details/78729132?utm_source=app&app_version=4.11.0&code=app_1562916241&uLinkId=usr1mkqgl919blen
"""

# header 用来伪装浏览器发送请求
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'}
url = 'http://www.biqikan.com/45/45156/20084884.html'
req = requests.get(url)  # 向目标网站发送 get 请求
# print("文件编码：", req.encoding)  # gbk
# print("响应状态码：", req.status_code)  # 200
# print("字符串的响应体：", req.text)

result = req.content
# 查看网页源代码 charset=gbk , 即网页用的是 gbk 编码， 故要用 gbk 的编码方式来解码， 否则中文会乱码
result = result.decode('gbk')

title_re = re.compile(r'<li class="active">(.*?)</li>')  # 取出文章标题
text_re = re.compile(r'<br><br>([\s\S]*?)</div>')  # 由于正文部分有很多的换行符，故使用 [\s\S]
title = re.findall(title_re, result)  # 找出标题
text = re.findall(text_re, result)  # 找出正文
# title = title[0]  # 由于返回的 title 是列表，故取出列表的第一项
print(title)  # 打印出标题



print(result)

