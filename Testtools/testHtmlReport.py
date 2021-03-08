#coding=utf-8
'''
Created on 2019年1月13日

@author: yangkai
'''

import json


def HTMLReporttest(ResultReport):
    startTime = ResultReport['startTime']
    endTime = ResultReport['endTime']
    executionTime = ResultReport['executionTime']
    listSum = ResultReport['listSum']
    passSum = ResultReport['passSum']
    Pass = ResultReport['Pass']
    fillSum = ResultReport['fillSum']
    Fill = ResultReport['Fill']
    passAllSum = ResultReport['passAllSum']
    startPass = ResultReport['startPass']
    startFillSum = ResultReport['startFillSum']
    startFill = ResultReport['startFill']
    startReport = ResultReport['startReport']
    endReport = ResultReport['endReport']
    IntegrationReport = []
    startReportDict = []
    endReportDict = []
    
    for Report in startReport:
        Result = {
            'className': Report[1],
            'methodName': Report[2],
            'description': Report[3],
            'status': Report[4],
            'log': Report[5],
            }
        startReportDict.append(Result)
    print('startReportDict: ', startReportDict)
    if endReport:
        for Report in endReport:
            Result = {'className': Report[1],
                    'methodName': Report[2],
                    'description': Report[3],
                    'status': Report[4],
                    'log': Report[5]}
            endReportDict.append(Result)
    
    if endReport:
        for start in startReportDict:
            for end in endReportDict:
                if start['description'] == end['description']:
                    start = end
                    break
            IntegrationReport.append(start)
    else:
        IntegrationReport = startReportDict
        passAllSum = passSum
        startFillSum = fillSum


    Result = {
        'startTime': startTime,
        'endTime': endTime,
        'executionTime': executionTime,
        'listSum': listSum,
        'passSum': passSum,
        'Pass': Pass,
        'fillSum': fillSum,
        'Fill': Fill,
        'passAllSum': passAllSum,
        'startPass': startPass,
        'startFillSum': startFillSum,
        'startFill': startFill,
        'startResult': startReport,
        'endResult': endReport,
        'IntegrationReport': IntegrationReport
    }
    Result = json.dumps(Result)
    with open('../Testdata/template.html', 'rb') as fo:
        lines = fo.read()
        fo.close()
    lines = lines.replace(b'Edit_resultData', Result.encode('utf-8'))
    with open('../Report/CaseReport.html', 'wb') as fo:
        fo.write(lines)
        fo.close()
















