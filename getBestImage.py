import requests
from base64 import b64encode
import json


API_KEY = 'AIzaSyAreWgIuI0PMa0cjlAexGbp4En-gYc-zn0'
cx = '009536253110487065281:x6pbmstcpy8'

def getLabel(img):
    payload = {'key':API_KEY}
    url = "https://vision.googleapis.com/v1/images:annotate"
    data = {
        "requests": [
            {
                "image": {
                    "source": {
                        "imageUri": img
                    }
                },
                "features": [
                    {
                        "type": "WEB_DETECTION",
                        "maxResults": 1
                    }
                ]
            }
        ]
    }
    r = requests.post(url, params=payload, json=data)
    result = r.json()
    print(result)
    return result['responses'][0]['webDetection']['webEntities'][0]['description']

def takoyaki(img_lists):
    results = []
    for img in img_lists:
        results.append(getLabel(img))
    
    return results

images =  [
      "https://imgfp.hotp.jp/IMGH/00/13/P032000013/P032000013_480.jpg", 
      "https://imgfp.hotp.jp/IMGH/31/12/P032313112/P032313112_480.jpg", 
      "https://imgfp.hotp.jp/IMGH/30/90/P032313090/P032313090_480.jpg", 
      "https://imgfp.hotp.jp/IMGH/30/96/P032313096/P032313096_480.jpg", 
      "https://imgfp.hotp.jp/IMGH/50/18/P031975018/P031975018_480.jpg", 
      "https://imgfp.hotp.jp/IMGH/31/07/P032313107/P032313107_480.jpg", 
      "https://imgfp.hotp.jp/IMGH/50/21/P031975021/P031975021_480.jpg"
    ]

print(takoyaki(images))