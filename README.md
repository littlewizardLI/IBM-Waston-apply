# waston-making-poem
这是一个基于bluemix平台，利用Waston开发的，根据图片内容作诗的项目。
项目主要有三个部分：
 - 获取图片并识别。利用微信公众平台获得图片，而后调用Watson的图像识别服务。
 - 根据图片内容进行转义。因为Watson返回的结果是英文的。所以我将英文内容翻译成了中文。
 - 作诗。将中文内容设为关键字，在网上爬取相关古诗词。并返回给用户。
具体的实现，过段 时间我会写个较完整的文章出来

（目前该功能已关闭，我正在重构这个项目，准备加上waston的语音输出，这样就能把诗念出来，以及加上一些符合情境的对话）

this project can make a poem according the picture's content,using Waston. 

