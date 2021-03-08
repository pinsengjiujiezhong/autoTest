# coding=utf-8
'''
Created on 2018年6月10日

@author: Administrator
'''


from object import *
from Testtools.testMailReport import *
from Testcase.Login import *
from Testcase.zimu.material import *


def runCase(mainName,driver):
    Boole = eval(mainName)(driver)
    return Boole


def autoCase(caseLists,shotPath,reportPath,statisticalPath,mailDict,Priority = 3):
    mianPage = pythonFun()
    # 高优先级用例列表
    highPriorityCaseList = []
    # 中优先级列表
    modestPriorityCaseList = []
    # 低优先级列表
    lowPriorityCaseList = []
    # 初次执行报表
    startReports = []
    # 重跑执行报表 
    endReports = []
    for caseList in caseLists:
        if caseList[4] == '1':
            highPriorityCaseList.append(caseList)
        elif caseList[4] == '2':
            modestPriorityCaseList.append(caseList)
        elif caseList[4] == '3':
            lowPriorityCaseList.append(caseList)
    # 总优先级列表
    PriorityCaseLists = []
    if Priority == 1:
        PriorityCaseLists.append(highPriorityCaseList)
    elif Priority == 2:
        PriorityCaseLists.append(highPriorityCaseList)
        PriorityCaseLists.append(modestPriorityCaseList)
    elif Priority == 3:
        PriorityCaseLists.append(highPriorityCaseList)
        PriorityCaseLists.append(modestPriorityCaseList)
        PriorityCaseLists.append(lowPriorityCaseList)
    else:
        raise ValueError('优先级设置错误')
    # 自动化用例开始执行时间
    strattimestamp = time.time()
    for PriorityCaseList in PriorityCaseLists:
        for case in PriorityCaseList:
            log = True
            try:
                driver = Login()
                Boole = runCase(case[3], driver)
            except Exception as e:
                log = str(e).replace('\n', '')
                Boole = False
            searchPage = SeleniumFun(driver)
            if not Boole:
                shot = shotPath + '\\' + case[3] + '.png'
                searchPage.getScreenshotAsFile(shot)
            driver.quit()
            print('log: ', log)
            startReports.append([case[0],case[1],case[2],case[3],Boole,log])
            mianPage.writeCsv(reportPath, [case[0],case[1],case[2],case[3],Boole,log])
    reportLists = mianPage.readCsv(reportPath)
    heavyRunList = []
    for reportList in reportLists:
        print('reportList: ', reportList)
        # reportList[3]为自动化用例函数名称
        # reportList[4]为自动化用例执行结果
        if reportList[0]:
            if reportList[4] == 'False':
                print('当前已经执行')
                heavyRunList.append(reportList)
    # 有失败的自动化用例既重跑
    if len(heavyRunList):
        for i in range(4):
            mianPage.writeCsv(reportPath,[''])
        mianPage.writeCsv(reportPath,['重跑的用例'.encode('gbk')])
        for case in heavyRunList:
            log = True
            try:
                driver = Login()
                Boole = runCase(case[3], driver)
            except Exception as e:
                log = str(e).replace('\n', '')
                Boole = False
            searchPage = SeleniumFun(driver)
            if not Boole:
                shot = shotPath + '\\' + case[3] + '.png'
                searchPage.getScreenshotAsFile(shot)
            driver.quit()
            print('log: ', log)
            endReports.append([case[0], case[1], case[2], case[3], Boole, log])
            mianPage.writeCsv(reportPath, [case[0], case[1], case[2], case[3], Boole, log])
    else:
        endReports = []
    # 自动化用例结束执行时间
    endtimestamp = time.time()
    ResultReport = mianPage.Statistical(strattimestamp, endtimestamp, reportPath,statisticalPath,startReports,endReports)
    sendMail(mailDict,ResultReport)
    return 
    
    
def main(modules):
    mailDict = {
        'sender': '841346559@qq.com',
        'receiver': '13533630193@163.com',
        'subject': 'subject',
        }
    mianPage = pythonFun()
    # 自动化测试报告明细保存路径
    reportPath = '../Report/customerReport.csv'
    # 自动化测试报告文件路径        
    statisticalPath = '../Report/customerStatistical.csv'
    # 自动化测试错误截图路径
    shotPath = '../ScreenShot'
    # 自动化用例文件路径
    casePath = '../Testdata/groupClassName.csv'
    mianPage.Remove(reportPath)     
    mianPage.Remove(statisticalPath)
    mianPage.Shutil(shotPath)
    mianPage.Mkdir(shotPath)
    cases = []
    caseLists = mianPage.readCsv(casePath)
    for caseList in caseLists:
        if caseList[1] in modules:
            cases.append(caseList)
    autoCase(cases,shotPath,reportPath,statisticalPath,mailDict)

    
if __name__ == '__main__':
#      driver = Login()
#      Boole = runCase('newAttachmentGroup', driver)
#      print Boole
    mianPage = pythonFun()
    strattimestamp = 0
    endtimestamp = 0
    reportPath = 'G:\\Python\\PythonWriter\\customerReport.csv'    
    # 自动化测试报告文件路径        
    statisticalPath = 'G:\\Python\\PythonWriter\\customerStatistical.csv'
    # 自动化测试错误截图路径
    mianPage.Statistical(strattimestamp, endtimestamp, reportPath, statisticalPath)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    