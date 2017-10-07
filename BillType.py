import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='Credentials.json'

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

file_name = os.path.join(
    os.path.dirname(__file__),
    'images/1.jpg')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.logo_detection(image=image)
logos = response.logo_annotations

for logo in logos:
    if (logo.score > 0.6):
        print(logo.description)
