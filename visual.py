# -*- coding: utf-8 -*-
# filename: visrecognition.py

import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3


#url = "http://mmbiz.qpic.cn/mmbiz_jpg/ZTBrB9aVTqWUd5p1xnbnOnKicWTDuibZVA2JHQH2jbicNBia91vXwpLsrb7flMElNRstUfj3joXzLYYUub7OWaWL0A/0"

def VisualContent(url):
  visualRecognition = VisualRecognitionV3('2016-05-20', api_key='56ddbf9546c752bbb40fb04fa35b15d71c68032e')

  content = visualRecognition.classify(images_url = url)

  images = content.get("images")
  classifiers = images[0].get("classifiers")
  classes = classifiers[0].get("classes")
  res = classes[0].get("class")
  

  return res

#answer = content.get("images").get("classifiers")
#print(content)
#print("\n")
#print(content.keys())
#print("\n")
#print(images)
#print("classifiers:  \n")
#print(classifiers)
#print("\n res:")
#print(res)