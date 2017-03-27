# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, request, make_response  
import hashlib
import receive, reply, visual, translate, poem
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/check',  methods=['GET', 'POST'])  
def check():  
    if request.method == 'GET':  
        token = 'changshunowcs'   
        signature = request.args.get('signature', '')  
        echostr = request.args.get('echostr', '')  
        timestamp = request.args.get('timestamp', '')  
        nonce = request.args.get('nonce', '')  
        tmp = [timestamp, nonce, token]  
        tmp.sort()  
        tmp = ''.join(tmp)  
        if ( hashlib.sha1(tmp).hexdigest() == signature ):    
            return make_response(echostr)  
    else:
        recMsg = receive.parse_xml(request.stream.read())
        if isinstance(recMsg, receive.Msg):
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.MsgType == 'text':
                textContent1 = recMsg.Content
                textContent2 = translate.Translate(textContent1)
                textContent3 = poem.MakePoem(textContent2)
                replyMsg = reply.TextMsg(toUser, fromUser, textContent3)
                return replyMsg.send()
            if recMsg.MsgType == 'image':
                mediaId = recMsg.MediaId
                mediaUrl = recMsg.PicUrl
                imgContent1 = visual.VisualContent(mediaUrl)
                imgContent2 = translate.Translate(imgContent1) 
                content = poem.MakePoem(imgContent2)
                #content = "url: " + mediaUrl
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                return reply.Msg().send()
        else:
            print ("...")
            return reply.Msg().send()
        
        
port = os.getenv('PORT', '8000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
