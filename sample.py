import cognitive_face as CF

KEY = '0f4b97a384544170ac4b30161f48daa1'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

def fetch_faceid(image_url):
    result = CF.face.detect(image_url)
    return result[0]['faceId']

img_url = 'https://avatars2.githubusercontent.com/u/1504952?v=3&s=460'
face1 = fetch_faceid(img_url)

img_url = 'https://a248.e.akamai.net/secure.meetupstatic.com/photos/member/4/8/d/c/member_230958652.jpeg'
face2 = fetch_faceid(img_url)

result = CF.face.verify(face1, face2)
print result

