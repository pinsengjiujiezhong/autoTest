#coding=utf-8
'''
Created on 2018年5月21日

@author: Administrator
'''
from selenium import webdriver
import time, re, csv, os, shutil
import random, pymysql
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.action_chains import ActionChains
from Testtools.testHtmlReport import *
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twisted.persisted.aot import Instance
from Testtools.testHtmlReport import *


class SeleniumFun(object):
    
    def __init__(self, driver, base_url='https:\\pf.winbons.com'):
        self.driver = driver
#         self.base_url = base_url
    
    def imWait(self, time_out):
        self.driver.implicitly_wait(time_out)
        
    def find_element(self, elementLocal):
        result = elementLocal.split('=>')
        if result[0] == 'css':
            return self.driver.find_element_by_css_selector(result[1])
        elif result[0] == 'xpath':
            return self.driver.find_element_by_xpath(result[1])
        else:
            raise ValueError('当前定位的元素错误')
    
    def find_elements(self, elementLocal, pop=False, Positive=True, nubmer=1):
        result = elementLocal.split('=>')
        elementGroup = self.driver.find_elements(result[0], result[1])
        if pop:
            for i in range(nubmer):
                if Positive:
                    elementGroup.pop(0)
                else:
                    elementGroup.pop()
        return elementGroup
    
    def click(self, elements):
        SeleniumFun.find_element(self,  elements).click()

    def clear(self, elements):
        SeleniumFun.find_element(self,  elements).clear()
        
    def sendKey(self, elements, value):
        SeleniumFun.find_element(self,  elements).send_keys(value)

    def getText(self, elements):
        return SeleniumFun.find_element(self,  elements).text

    def scrollIntoView(self, location=10000):
        js="var q=document.documentElement.scrollTop=%d"%location
        self.driver.execute_script(js)  
    
    def executeScript(self, Js):
        self.driver.execute_script(Js)
    
    def getAttr(self, attrtext, elementLocal):
        element = SeleniumFun.find_element(elementLocal)
        attevalue = element.get_attribute(attrtext)
        return attevalue
        
    def switchTowindow(self, title):        #切换页签
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to_window(handle)
            if self.driver.title == title:
                break
        else:
            raise ValueError

    def switchToAlert(self, Boole=True):                    #警告框处理
        if Boole:
            self.driver.swtich_to_alert().accept()
        else:
            self.driver.swtich_to_alert().dismiss()

    def switchToFrame(self, elementLocal):            #切换iframe
        frame = SeleniumFun.find_element(elementLocal)
        self.driver.switch_to_frame(frame)

    def switchToDefaultContent(self):            #结束当前iframe
        self.driver.switch_to.default_content()

    def switchToParentFrame(self):                #切换至上层iframe
        self.driver.switch_to.parent_frame()

    #在当前焦点操作
    def switchToActiveElement(self, value):
        self.driver.switch_to.active_element.send_keys(value)  

    def getScreenshotAsFile(self, Path):           #屏幕截图
        self.driver.get_screenshot_as_file(Path)
        
    def moveToElement(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        
    def contextClick(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()
    
    def doubleClick(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()
    
    #左键长按
    def clickAndHold(self, element):  
        action = ActionChains(self.driver)
        action.click_and_hold(element).perform()
    
    def dragAndDrop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def textCheck(self, elements, text, flag=True):
        if flag:
            for element in elements:
                if text in element.text:
                    return True
            return False
        elif not flag:
            for element in elements:
                if text in element.text:
                    return False
            return True
        else:
            raise ValueError
    

        

class pythonFun(object):
    def __init__(self):
        pass
        
    def readCsv(self, Path):             #读取CSV文件
        with open(Path, 'r',  encoding='utf-8') as fo:
            lines = fo.readlines()
            fo.close()
            lists = []
            for line in lines:
                line = line.strip()
                list = line.split(', ')
                lists.append(list)
            return lists
    
    def readTxt(self, Path):
        with open(Path,  'rb',  encoding='utf-8') as fo:
            lines = fo.readlines()
            fo.close()
            lists = []
            for line in lines:
                line = line.strip()
                lists.append(line)
            return lists

    # 针对CSV文件追加写入
    def writeCsv(self,  Path,  values,  way='a'):
        with open(Path,  way,  encoding='utf-8',  newline='') as fo:
            writer = csv.writer(fo)
            writer.writerow(values)
            fo.close()
    
    def timeStamp(self):
        datatime = int(time.time())
        return datatime
    
    def Upload(self, Path):
        os.system(Path)
        
    def Remove(self, Path):
        try:
            os.remove(Path)
        except:
            pass
    
    def Shutil(self, Dir):
        try:
            shutil.rmtree(Dir)
        except:
            pass
        
    def Mkdir(self, Dir):
        try:
            os.mkdir(Dir)
        except:
            pass

    def Bj_time(self, now_time):
        now_time = int(now_time)
        localtime = time.localtime(now_time)
        strftime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
        return strftime
    
    def currentTime(self, strat=0, end=-1):
        now_time = int(time.time())
        localtime = time.localtime(now_time)
        strftime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
        return strftime[strat:end]
    
    def Statistical(self, strattimestamp, endtimestamp, reportPath, statisticalPath, startReports, endReports):
        passSum = 0 #用例执行初始通过数
        fillSum = 0 #用例执行初始失败数
        startPassSum = 0  #用例执行重跑通过数
        startFillSum = 0  #用例执行重跑失败数
        passAllSum = passSum
        reportList = pythonFun.readCsv(self, reportPath)
        for startReport in startReports:
            if startReport[4]:
                passSum += 1 
            elif not startReport[4]:
                fillSum += 1
        if endReports:
            for list in endReports:
                if list[4]:
                    startPassSum += 1 
                elif not list[4]:
                    startFillSum += 1
        listSum = passSum + fillSum    #用例执行初始总数
        Pass = '%.2f%%'%(float(passSum) / float(listSum) * 100)   #用例执行初始通过率
        Fill = '%.2f%%'%(float(fillSum) / float(listSum) * 100)   #用例执行初始失败率
        if endReports:
            startPass = '%.2f%%'%(float(passSum + startPassSum) / float(listSum) * 100)     #用例执行重跑通过率
            startFill = '%.2f%%'%(float(startFillSum) / float(listSum) * 100)               #用例执行重跑失败率
        else:
            startPass = Pass
            startFill = Fill
        starttime = pythonFun.Bj_time(self, strattimestamp)
        endtime = pythonFun.Bj_time(self, endtimestamp)
        with open(statisticalPath,  'a',  newline='') as fo:
            writer = csv.writer(fo)
            writer.writerow(['执行开始时间', starttime, '执行结束时间', endtime])
            executionTimeSec = int(endtimestamp-strattimestamp)
            hour = executionTimeSec / 3600
            min = executionTimeSec % 3600 / 60
            sec = executionTimeSec % 3600 % 60
            executionTime = '%d时%d分%d秒'%(hour, min, sec)
            writer.writerow(['耗时（秒）', executionTime])
            writer.writerow(['用例总数', str(listSum)])
            writer.writerow(['用例初始通过数', str(passSum), '用例初始通过率', Pass])
            writer.writerow(['用例初始失败数', str(fillSum), '用例初始失败率', Fill])
            if endReports:
                passAllSum = passSum + startPassSum
                writer.writerow(['用例重跑后通过数', str(passAllSum), '用例重跑通过率', startPass])
                writer.writerow(['用例重跑后失败数', str(startFillSum), '用例重跑失败率', startFill])
            for i in range(3):
                writer.writerow([''])
            writer.writerow(['用例详细报告'])
            reportLists = pythonFun.readCsv(self, reportPath)
            for reportList in reportLists:
                writer.writerow(reportList)
            fo.close()
        ResultReport = {
            'startPass': startPass, 
            'startFillSum': startFillSum, 
            'startFill': startFill, 
            'startReport': startReports, 
            'endReport': endReports, 
            'startTime': starttime, 
            'endTime': endtime, 
            'executionTime': executionTime, 
            'listSum': listSum, 
            'passSum': passSum, 
            'Pass': Pass, 
            'fillSum': fillSum, 
            'Fill': Fill, 
            'passAllSum': passAllSum, 
        }
        print('ResultReport:',  ResultReport)
        HTMLReporttest(ResultReport)
        return ResultReport

    def test(self):
        strattimestamp = time.time()
        strattime = pythonFun.Bj_time(self, strattimestamp)


if __name__ == '__main__':
    mainPage = pythonFun()
    mainPage.test()

