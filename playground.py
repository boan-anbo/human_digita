import base64
import json

from django.core.files.base import ContentFile


def base64_to_imagefield_content(data) -> ContentFile:
    format, imgstr = data.split(';base64,')  # format ~= data:image/X,
    ext = format.split('/')[-1]  # guess file extension

    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    return data


if __name__ == '__main__':
    with open(
        r'C:\Users\Bo\Documents\extracted_pdf_full_texts\[R] [[15ODJS-11Ji74]] 1974 - 15O(DJS—11)机的软件.json', 'r', encoding='UTF-8') as json_file:
        data = json.load(json_file)

        fh = open("imageToSave.png", "wb")
        annotations = data.get('annotations', None)
        for annotation in annotations:
            image = annotation.get('image', None)
            if image:
                print(image)
                image_data = base64.b64decode(image)
                # fh.write(image_data)
                base64_to_imagefield_content(data)
