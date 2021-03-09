import json
import os
import threading
import queue

import requests

def send_json(json):
    newHeaders = {'Content-type': 'application/json'}
    r = requests.post("http://localhost:8000/api/documents/post_document/", json=json, headers=newHeaders)
    # print(r)
    return r
def star_send_json(q, json):
    q.put(send_json(json))
def upload_documents():
    path_to_json = r'C:\extracted_pdf_annotations_and_fulltexts'
    count = 0
    q = queue.Queue()

    for file in os.listdir(path_to_json):
        full_filename = "%s\%s" % (path_to_json, file)
        with open(full_filename, 'r', encoding='UTF-8') as fi:
            doc = json.load(fi)
            annotations = doc.get('annotations', None)
            if annotations and len(annotations) > 0:
                try:
                    r = send_json(doc)
                    print(full_filename)
                    print(r)
                except Exception as e:
                    print(e)
                    continue

                # if count < 10:
                    # print(doc)
                # t = threading.Thread(target=star_send_json, args=(q, doc))
                # t.daemon = True
                # t.start()
    s = q.get()
    print(s)

if __name__ == '__main__':
    upload_documents()
