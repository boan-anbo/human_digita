import json
import os
import threading
import queue

import requests

def send_json(json):
    newHeaders = {'Content-type': 'application/json'}
    r = requests.post("http://localhost:8010/api/passages/post_passages/", json=json, headers=newHeaders)
    # print(r)
    return r
def upload_documents():
    path_to_json = r'C:\extracted_pdf_annotations_and_fulltexts'
    count = 0
    q = queue.Queue()

    for file in os.listdir(path_to_json):
        full_filename = "%s\%s" % (path_to_json, file)
        with open(full_filename, 'r', encoding='UTF-8') as fi:
            doc = json.load(fi)
            fulltexts = doc.get('fullTexts', None)
            if fulltexts and len(fulltexts) > 0:
                try:
                    # if count < 2:
                    r = send_json(doc)
                        # print(doc)
                    print(full_filename)
                    print(r.status_code.__str__() + ': ' +  full_filename)
                        # count += 1
                    # print(r)
                except Exception as e:
                    print(e)
                    continue


if __name__ == '__main__':
    upload_documents()
