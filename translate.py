import urllib.request
import urllib.parse
import json 

def Translate(word):
  url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
  key = word

  data = {}
  data['type'] = 'AUTO'
  data['i'] = key
  data['doctype'] = 'json'
  data['xmlVersion'] = '1.6'
  data['keyfrom'] = 'fanyi.web'
  data['ue'] = 'UTF-8'
  data['typoResult'] = 'true'

  data = urllib.parse.urlencode(data).encode("utf-8")
  content = urllib.request.urlopen(url, data).read().decode("utf-8")
  json_content = json.loads(content)
  res = json_content["translateResult"][0][0]['tgt'][:2]

  return res

#print(content)
#print(res)
