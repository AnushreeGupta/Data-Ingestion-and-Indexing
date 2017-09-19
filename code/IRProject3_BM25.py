# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""

import json
import urllib.request
import codecs

count = 1
with codecs.open('/home/anushree/Desktop/IRProject3/queries.txt', encoding='utf-8') as f:
    for line in f:
        query = line.strip('\n').replace(':', '')
        query = urllib.parse.quote(query)
        inurl = 'http://localhost:8983/solr/BM25/select?defType=edismax&fl=id,score&indent=on&q='+query+'&qs=70&rows=200&tie=0.1&wt=json'
        qid = count
        IRModel = 'BM25'
        outf = open('/home/anushree/Desktop/IRProject3/trec_eval.9.0/Outputs/'+str(count)+'.txt', 'a+')
        data = urllib.request.urlopen(inurl).read()
        docs = json.loads(data.decode('utf-8'))['response']['docs']
        rank = 1
        for doc in docs:
            if count < 10:
                outf.write('00'+str(qid) + ' ' + 'Q' + str(count) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + 'BM25' + '\n')
            else:
                outf.write('0'+str(qid) + ' ' + 'Q' + str(count) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + 'BM25' + '\n')
            rank += 1
        outf.close()
        count += 1


