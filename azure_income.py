import requests
import json

subscription_key = '67b76f5db2304c54918fb388dbea7ca3'
assert subscription_key == '67b76f5db2304c54918fb388dbea7ca3'

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type':'application/octet-stream'}
data=open('/home/pi/savedimage.jpg','rb').read()

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, data=data)
print(json.dumps(response.json()))