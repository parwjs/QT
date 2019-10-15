from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import random
import time


browser = webdriver.Chrome()
browser.get("https://www.wjx.cn/jq/47586489.aspx")

grade_list = ['//*[@id="divquestion1"]/ul/li[1]/a','//*[@id="divquestion1"]/ul/li[2]/a',
              '//*[@id="divquestion1"]/ul/li[3]/a','//*[@id="divquestion1"]/ul/li[4]/a']

age_list = ['20','21','22','24','23','25']

major_list = ['//*[@id="divquestion3"]/ul/li[1]/a','//*[@id="divquestion3"]/ul/li[3]/a',
              '//*[@id="divquestion3"]/ul/li[2]/a','//*[@id="divquestion3"]/ul/li[4]/a',
              '//*[@id="divquestion3"]/ul/li[5]/a','//*[@id="divquestion3"]/ul/li[6]/a',\
              '//*[@id="divquestion3"]/ul/li[7]/a','//*[@id="divquestion3"]/ul/li[8]/a']

majors = ['哲学','经济学','管理学','教育学']


know_list = ['//*[@id="divquestion4"]/ul/li[1]/a','//*[@id="divquestion4"]/ul/li[2]/a']

year_list = ['//*[@id="divquestion5"]/ul/li[1]/a','//*[@id="divquestion5"]/ul/li[2]/a',
             '//*[@id="divquestion5"]/ul/li[3]/a','//*[@id="divquestion5"]/ul/li[4]/a']

from_know = ['//*[@id="divquestion6"]/ul/li[1]/a','//*[@id="divquestion6"]/ul/li[2]/a',
             '//*[@id="divquestion6"]/ul/li[3]/a','//*[@id="divquestion6"]/ul/li[4]/a',
             '//*[@id="divquestion6"]/ul/li[5]/a','//*[@id="divquestion6"]/ul/li[6]/a']

from_knows = [2,3,4,5,6]

popularize_list = ['//*[@id="divquestion7"]/ul/li[1]/a','//*[@id="divquestion7"]/ul/li[2]/a']

influence_list = ['//*[@id="divquestion8"]/ul/li[1]/a','//*[@id="divquestion8"]/ul/li[2]/a',
                  '//*[@id="divquestion8"]/ul/li[3]/a']

work_list = ['//*[@id="divquestion9"]/ul/li[1]/a','//*[@id="divquestion9"]/ul/li[2]/a',
             '//*[@id="divquestion9"]/ul/li[3]/a','//*[@id="divquestion9"]/ul/li[4]/a',
             '//*[@id="divquestion9"]/ul/li[5]/a','//*[@id="divquestion9"]/ul/li[6]/a',
             '//*[@id="divquestion9"]/ul/li[7]/a']
works = [2,3,3,4,5,6,7]

facts_list = ['//*[@id="divquestion10"]/ul/li[1]/a','//*[@id="divquestion10"]/ul/li[2]/a',
         '//*[@id="divquestion10"]/ul/li[3]/a','//*[@id="divquestion10"]/ul/li[4]/a',
         '//*[@id="divquestion10"]/ul/li[5]/a','//*[@id="divquestion10"]/ul/li[6]/a',
         '//*[@id="divquestion10"]/ul/li[7]/a']

lazy_list = ['//*[@id="divquestion11"]/ul/li[1]/a','//*[@id="divquestion11"]/ul/li[2]/a',
             '//*[@id="divquestion11"]/ul/li[3]/a']


company_list = ['//*[@id="divquestion12"]/ul/li[1]/a','//*[@id="divquestion12"]/ul/li[2]/a',
                '//*[@id="divquestion12"]/ul/li[3]/a','//*[@id="divquestion12"]/ul/li[4]/a',
                '//*[@id="divquestion12"]/ul/li[5]/a','//*[@id="divquestion12"]/ul/li[6]/a',
                '//*[@id="divquestion12"]/ul/li[7]/a','//*[@id="divquestion12"]/ul/li[8]/a',
                '//*[@id="divquestion12"]/ul/li[9]/a','//*[@id="divquestion12"]/ul/li[10]/a',
                '//*[@id="divquestion12"]/ul/li[11]/a']

companys = [2,3,4,5,6,7,8,9,10,11]


think_list = ['//*[@id="divquestion13"]/ul/li[1]/a','//*[@id="divquestion13"]/ul/li[2]/a',
              '//*[@id="divquestion13"]/ul/li[3]/a']


submit_button = '//*[@id="submit_button"]'

def select_more(needList,conditionList):
    randomMore = get_randomValue2(needList,conditionList)
    for i in randomMore:
        browser.find_element_by_xpath(i).click()

def select_less(needList):
    browser.find_element_by_xpath(get_randomValue(needList)).click()

def write_less(xpath,randomList):
    browser.find_element_by_xpath(xpath).send_keys(get_randomValue(randomList))

# 如果选到其他就填入预先设定好的随机值
def select_ConditionLess(needList,condition,doString,okList):
    randomString = get_randomValue(needList)
    if randomString == condition :
        browser.find_element_by_xpath(doString).send_keys(get_randomValue(okList))
    else:
        browser.find_element_by_xpath(randomString).click()

# 得到随机数
def get_randomValue(list):
    return random.choice(list)

def get_randomValue2(list1,list2):
    return random.choices(list1,k=random.choice(list2))


def select() :
    # 年级
    select_less(grade_list)
    time.sleep(0.1)

    # 年龄
    write_less('//*[@id="q2"]', age_list)
    time.sleep(0.1)

    # 专业
    select_ConditionLess(major_list, '//*[@id="divquestion3"]/ul/li[8]/a', '//*[@id="divquestion3"]/ul/li[8]/input[2]',
                         majors)
    time.sleep(0.1)

    # 了解程度
    select_less(know_list)
    time.sleep(0.1)
    # 普及年数
    select_less(year_list)
    time.sleep(0.1)
    # 哪里听过这个词汇
    select_more(from_know, from_knows)
    time.sleep(0.1)
    # 觉得普及
    select_less(popularize_list)
    time.sleep(0.1)
    # 产生影响

    select_less(influence_list)
    time.sleep(0.1)
    # 取代工作
    select_more(work_list, works)
    time.sleep(0.1)
    # 应用在哪些方面
    select_more(facts_list, works)
    time.sleep(0.1)
    # 增加惰性
    select_less(lazy_list)
    time.sleep(0.1)
    # 哪些公司
    select_more(company_list, companys)
    time.sleep(0.1)
    # 考虑过
    select_less(think_list)

    time.sleep(2)
    # 提交
    browser.find_element_by_xpath(submit_button).click()

def open_new():
    js = 'window.open("https://www.wjx.cn/jq/47586489.aspx")'
    browser.execute_script(js)




if __name__ == '__main__':

    for i in range(30):
        select()
        result = EC.alert_is_present()(browser)
        if result:
            time.sleep(15)
        else:
            time.sleep(3)
        open_new()
        handles = browser.window_handles
        browser.close()
        browser.switch_to_window(handles[1])



time.sleep(3)
browser.quit()










