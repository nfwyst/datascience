#!/usr/bin/env python3
# coding:utf8
import sys
import json

stream = open('test.txt', 'r')

characters = []
dics = {}

'''
统计
'''
for line in stream:
    line = line.strip()
    if len(line) == 0:
        continue
    line = str(line)
    for x in range(0, len(line)):
        if line[x] in ['[',']',',','.',' ','\t','\n']:
            continue
        if not line[x] in characters:
            characters.append(line[x])
        if not line[x] in dics:
            dics[line[x]] = 0
        dics[line[x]] += 1

'''
json
'''
js = open('result.json', 'w')
js.write(json.dumps(dics))
js.close()

'''
按频率排序
'''
dics = sorted(dics.items(), key=lambda d:d[1], reverse=True)

'''
csv
'''
writer = open('result.csv', 'w')
for item in dics:
    writer.write(item[0] + ',' + str(item[1]) + '\n')
writer.close()

stream.close()
