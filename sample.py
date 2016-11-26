import cognitive_face as CF
import base64
import os

KEY = os.environ['FACE_API_KEY']
CF.Key.set(KEY)

def fetch_faceid(image_url):
    result = CF.face.detect(image_url)
    return result[0]['faceId']

img_url = 'https://avatars2.githubusercontent.com/u/1504952?v=3&s=460'
face1 = fetch_faceid(img_url)

IMG_ON_FS='userimage.png'
file = open('base64imgtext', 'r')
with open(IMG_ON_FS, "wb") as fh:
  fh.write(base64.decodestring(file.read()))

result = CF.face.verify(face1, fetch_faceid(IMG_ON_FS))
print result

