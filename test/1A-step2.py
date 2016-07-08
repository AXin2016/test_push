# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:15:05 2016

@author: xinruyue
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

db = MongoClient("10.8.8.111:27017")['onions35']
topics = db['topics']

f = open('videoId.txt','r+')

videoId = []
for each in f:
    each = each.strip('\n')
    each = each.strip('"')
    videoId.append(ObjectId(each))

video_name = []
for each in videoId:
    print each
    video = list(topics.find({"_id":each}))[0]
    video_name.append(video['name'])
