import visual, translate, poem
from watson_developer_cloud import VisualRecognitionV3

#url = "http://mmbiz.qpic.cn/mmbiz_jpg/ZTBrB9aVTqWUd5p1xnbnOnKicWTDuibZVA2JHQH2jbicNBia91vXwpLsrb7flMElNRstUfj3joXzLYYUub7OWaWL0A/0"
url = "https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg"

print(VisualRecognitionV3('2016-05-20', api_key='56ddbf9546c752bbb40fb04fa35b15d71c68032e').classify(images_file = "D:/bjtu/1-style.jpg"))
content1 = visual.VisualContent(url)
content2 = translate.Translate(content1)
answer = poem.MakePoem(content2)


print("\n")
print(content1 + content2)
print("\n")
print(answer)