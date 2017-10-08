import os
import io
import glob

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='Credentials.json'

from google.cloud import vision
from google.cloud.vision import types

def billType(s):
    if "Lincoln" in s:
        return 5
    elif "Washington" in s:
        return 1
    elif "Jackson" in s:
        return 20
    elif "Hamilton" in s:
        return 10
    elif "Ulysses" in s:
        return 50
    elif "Franklin" in s:
        return 100
    else:
        return 0

def billValue(bill):
    client = vision.ImageAnnotatorClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        bill)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.web_detection(image=image)
    entities = response.web_detection

    for entity in entities.web_entities:
        value = billType(str(entity.description))
        if(value == 5 or value == 1):
            return value

    return 0

def total():
    total = 0

    for image in glob.glob('./faces/*'):
        total += billValue(image)
        os.remove(image)

    return total

print total()
