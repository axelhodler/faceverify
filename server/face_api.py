import cognitive_face as CF
import base64
import os

KEY = os.environ['FACE_API_KEY']
CF.Key.set(KEY)

def fetch_faceid(image_url):
    result = CF.face.detect(image_url)
    return result[0]['faceId']

def write_to_image(text, filename):
  with open(filename, "wb") as fh:
    fh.write(base64.decodestring(text))

def participants_match(image_participant_a, image_participant_b):
  img_src_a = 'participant_a.png'
  img_src_b = 'participant_b.png'
  write_to_image(image_participant_a, img_src_a)
  write_to_image(image_participant_b, img_src_b)
  verification = CF.face.verify(fetch_faceid(img_src_a), fetch_faceid(img_src_b))
  return str(verification['isIdentical']) + ':' + verification['confidence']
