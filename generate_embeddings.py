import os
import json
import numpy as np
import tensorflow as tf 
import tensorflow_hub as hub 
import textwrap
from time import time
from uuid import uuid4
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import re


def load_data(directory):
    files = os.listdir(directory)
    result = list()
    vectors = list()
    payloads = list()
    count = 0
    for file in files:
        count = count + 1
        with open('%s/%s' % (directory, file), 'r', encoding='utf-8') as infile:
            info = json.load(infile)
            vectors.append(info['embedding'])
            payloads.append({'content': info['string'], 'file': file})
        print(count, 'of', len(files), 'loaded')
    return vectors, payloads

def process_chunk(chunk):
    try:
        articles = list()
        strings = list()
        for article in chunk:
            info = json.loads(article)
            title = re.sub('\s+', ' ', info['title'].strip())
            abstract = re.sub('\s+', ' ', info['abstract'].strip())
            string = title + ' ' + abstract
            articles.append({'id':info['id'], 'title': title, 'abstract': abstract})
            strings.append(string)
        embeddings = embed(strings)
        vectors = embeddings.numpy().tolist()
        for i in list(range(0, len(chunk))):
            article = articles[i]
            article['embedding'] = vectors[i]
            save_data('embeddings', article)
    except Exception as oops:
        print(oops)
        save_data('errors', article)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_data(directory, payload):
    filename = '%s.json' % str(uuid4())
    with open('%s/%s' % (directory, filename), 'w', encoding='utf-8') as outfile:
        json.dump(payload, outfile, ensure_ascii=False, sort_keys=True, indent=1)


if __name__ == '__main__':
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

    arxiv = open_file('arxiv/arxiv-metadata-oai-snapshot.json').splitlines()
    print('Articles loaded:', len(arxiv))
    chunk_size = 200
    chunks = [arxiv[i:i + chunk_size] for i in range(0, len(arxiv), chunk_size)]
    total = len(chunks)
    print("Chunks to process: ", total)
    arxiv = list()
    count = 0
    start = time()
    for chunk in chunks:
        count = count + 1
        process_chunk(chunk)
        elapsed = time() - start
        avg = elapsed / count
        remaining = (total - count) * avg
        hours = remaining / 3600
        print(count, total - count, hours)








#             info = json.loads(article)
            
            

    
#     print('starting up...')
#     vectors, payloads = load_data('quib')

#     print('Starting Qdrant client...')
#     client = QdrantClient(host='192.168.50.171', port=6333)
    
#     print('Creating collection "stress_test"...')
#     #init collection
#     client.recreate_collection(
#         collection_name='stress_test',
#         vectors_config=VectorParams(size=512, distance=Distance.COSINE),
#     )

# # upload data
#     start = time()
#     print('Uploading records...')
#     client.upload_collection(
#     collection_name='stress_test',
#     vectors=vectors,
#     payload=payloads,
#     ids=None,
#     batch_size=256)
#     print("uploaded in", time() - start, "seconds.")









    # files = os.listdir('contexts/')
    # #print(files)
    # times = list()
    # for file in files:
    #     start = time()
    #     text = open_file('contexts/%s'% file)
    #     chunks = textwrap.wrap(text, 1000) # break file contents into chunks of 1000 chars
    #     embeddings = embed(chunks)
    #     vectors = embeddings.numpy().tolist()
    #     for i in list(range(0, len(chunks))):
    #         print(chunks[i], vectors[i])
    #         save_data({'string': chunks[i], 'embedding': vectors[i]})
    #     times.append(time() - start)
    #     print("Average time per file: ", sum(times)/len(times))
        