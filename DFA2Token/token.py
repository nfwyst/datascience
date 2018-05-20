#!/usr/bin/env python3
# coding:utf8

# 此法解析器的自动产生器, csv 中的规则对应的是能识别以 bb 或 aa 结尾的串, 且串中只能有a,b
# 初始状态和终止状态可配置
# DFA 文件名称可配置
# input 可配置
config = {
    'startState': 0,
    'endState': 3,
    'fileName': 'test.csv'
}
input = 'ababababaa'
pos = 0

def parseDFA():
    stateTransTable = []
    row = []

    stream = open(config['fileName'], 'r')

    for line in stream:
        line = line.strip()
        line = str(line)

        for item in line:
            if item == '\\':
                row.append(' ')
            elif item == ',':
                continue
            else:
                row.append(item)

        stateTransTable.append(row)
        row = []
    return stateTransTable

def find(target, value):
    for item in target:
        if item[0] == value:
            return target.index(item)
    return False

def getChar():
    global pos
    global input
    if pos == len(input):
        return False
    res = input[pos]
    pos += 1
    return res

def findCh(target, value):
    res = target[0]
    for item in res:
        if item == value:
            return res.index(item)
    return False

def nextToken():
    table = parseDFA()
    curState = str(config['startState'])
    result = ''

    # search Index of curState
    id = find(table, curState)
    ch = getChar()
    chId = findCh(table, ch)

    if not id or not ch or not chId:
        print(u'不能识别')
        return False

    while table[id][chId]:
        result += ch
        curState = table[id][chId]
        if curState == str(config['endState']):
            return result
        else:
            ch = getChar()
            chId = findCh(table, ch)
            id = find(table, curState)

            if not id or not ch or not chId:
                print(u'不能识别')
                return False

print(nextToken())
