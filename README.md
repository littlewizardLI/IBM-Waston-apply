# waston-making-poem
这是一个基于bluemix平台，利用Waston开发的，根据图片内容作诗的项目。
项目主要有三个部分：
 - 获取图片并识别。利用微信公众平台获得图片，而后调用Watson的图像识别服务。
 - 根据图片内容进行转义。因为Watson返回的结果是英文的。所以我将英文内容翻译成了中文。
 - 作诗。将中文内容设为关键字，在网上爬取相关古诗词。并返回给用户。
具体的实现，可以参加我的博客：https://segmentfault.com/u/chuanye

可以关注我的公众号Owcs，进行测试。（目前该功能已关闭，我正在重构这个项目）

this project can make a poem according the picture's content,using Waston. 

