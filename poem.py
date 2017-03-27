from lxml import etree
import requests
import sys

def MakePoem(word):
  url_base = "http://so.gushiwen.org/search.aspx?value="
  key = word
  url = url_base+key
  res = requests.get(url)
  res.encoding = 'utf-8'
  #print(res.text)
  root = etree.HTML(res.content)
  items = root.xpath('//div[@class="sons"][2]/p[@style="margin-bottom:0px;"]')[0]
  item = items.xpath('string(.)')
  
  content = item.replace('\n','').replace(' ','')
  length = len(content)
  answer = content[:length-1]

  return answer
  


#print(content)