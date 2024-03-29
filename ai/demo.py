# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/28 3:03 PM

# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/21 3:52 PM
import json

import requests


def buildRequest(text, imageUrl):
    return [{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": text
            }, {
                "type": "image_url",
                "image_url": {
                    "url": imageUrl,
                    "detail": "low"
                }
            }
        ]
    }]


# 注意，这里构造完multimodalRequest后，转成JSON字符串，放到params中的，
# key：multimodalRequest
# value：string of multimodalRequest

def buildData(multimodalRequest):
    return {
        "strategyId": 61120,
        "thirdPartyId": "marathon:3235a4e3-7ca8-b9fd-f991-3bae4fe3275d-2",
        "forRetry": False,
        "modelParams": "{\"modelName\":\"gpt-4-vision-preview\",\"serviceName\":\"openai\",\"supplier\":\"openai\",\"maxToken\":1000}",
        "stream": False,
        "bufferUntilSentence": False,
        "contextParams": {"identifyType": 2, "userIdentity": "liang02test"},
        "params": {
            "multimodalRequest": json.dumps(multimodalRequest)
        }
    }


headers = {
    "Content-type": "application/json"
}

if __name__ == '__main__':
    multimodalRequest = buildRequest("这个是什么，请给出符合此画内容和情景的中国古诗词有哪些?",
                                     "https://conan-test.cretacontent.com/conan-oss-resource/cjno5kv9t.webp")
    data = buildData(multimodalRequest)
    url = "http://ai-platform-test.zhenguanyu.com/conan-chat-ai/admin/api/chat/ai-chat/vision"
    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.text)
    responseText = json.loads(response.text)

    print(responseText['data'])
