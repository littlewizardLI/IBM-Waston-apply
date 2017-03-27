from lxml import etree
import requests
import sys

url_base = "http://so.gushiwen.org/search.aspx?value="
key = "樱桃"
url = url_base+key
res = requests.get(url)
res.encoding = 'utf-8'
#print(res.text)
root = etree.HTML(res.content)
items = root.xpath('//div[@class="sons"][2]/p[@style="margin-bottom:0px;"]')[0]
item = items.xpath('string(.)')
content =item.replace('\n','').replace(' ','').replace('▼','')

print(content)