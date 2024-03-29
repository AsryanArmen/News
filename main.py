from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

try:
        
    df = pd.DataFrame(columns = ['content', 'topic'])
    mli = []

    # driver.get('https://lenta.ru/')
    # time.sleep(3)

# # 0-rossia/obshestvo

#     driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(2) > a').click()
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._russia > a:nth-child(2)').click()
#     time.sleep(1)
   
#     for i in range(2, 91):
#         driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li.rubric-page__item._more > a > div.loadmore__button').click()
#         time.sleep(10)
#         driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li.rubric-page__item._more > a > div.loadmore__button').click()       
#         time.sleep(10)
#         driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
#         time.sleep(1)
#         text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
#         mli.append(text)
#         driver.back()
    
    '''            
    
    q = 0
#0 - rossia
    l_0 = 0
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(2) > a').click()
    time.sleep(1)
    for k in range(2, 8):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._russia > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 19):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_0 += 1
                driver.back()
            except:
                continue
    
    q = 1
# 1-ekonomika

    l_1 = 0
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(5) > a').click()
    time.sleep(1)
    for k in range(2, 9):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._economics > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 16):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_1 += 1
                driver.back()
            except:
                continue



    q = 2
# 2-silovie strukturi

    l_2 = 0
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(6) > a').click()
    time.sleep(1)
    for k in range(2, 6):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._forces > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 27):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_2 +=1
                driver.back()
            except:
                continue



    q = 3
# 3-sssr

    l_3 = 0
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(4) > a').click()
    time.sleep(1)
    for k in range(2, 8):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._ussr > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 19):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_3 += 1
                driver.back()
            except:
                continue



    q = 4
# 4 - sport
            
    l_4 = 0   
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(9) > a').click()
    time.sleep(1)
    for k in range(2, 10):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div.rubric-header._rubric-page > div.rubric-header__container._sport > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 15):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_4 += 1
                driver.back()
            except:
                continue


    q = 5
# 5 - zabota o sebe
            
    l_5 = 0            
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(15) > a').click()
    time.sleep(1)
    for k in range(2, 7):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._wellness > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 22):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_5 += 1
                driver.back()
            except:
                continue
            




    q = 7
# 7 - putishestviya
            
    l_7 = 0            
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(12) > a').click()
    time.sleep(1)
    for k in range(2, 7):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._travel > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 22):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_7 += 1
                driver.back()
            except:
                continue


    q = 8
# 8 - nauka

    l_8 = 0       
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout > div.layout__container > div.layout__header.js-layout-header > header > div.header__left > button').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#body > div.layout.js-layout._no-scroll > div.layout__menu > div > div.menu__container > nav > ul > li:nth-child(7) > a').click()
    time.sleep(1)
    for k in range(2, 13):
        driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > div > div.rubric-header__container._science > a:nth-child({k})').click()
        time.sleep(1)
    
        for i in range(2, 12):
            try:
                driver.find_element(By.CSS_SELECTOR, f'#body > div.layout.js-layout > div.layout__container > main > div.rubric-page > section > ul > li:nth-child({i}) > a > h3').click()
                time.sleep(1)
                text = driver.find_element(By.CLASS_NAME, "topic-body__content").text
                mli.append(text)
                l_8 += 1
                driver.back()
            except:
                continue

    '''            

    q = 6
#6 - stroitelstvo
    l_6 = 0
    driver.get('https://ria.ru/tag_thematic_category_Stroitelstvo/')
    time.sleep(3)

    for i in range(1, 101):
        try:
            driver.find_element(By.CSS_SELECTOR, f'#content > div > div.layout-rubric__main > div > div.list.list-tags > div:nth-child({i}) > div.list-item__content > a.list-item__title.color-font-hover-only').click()
            time.sleep(1)
            text = driver.find_element(By.CSS_SELECTOR, "#endless > div.endless__item.m-active > div > div > div > div.layout-article__over > div.layout-article__main > div > div:nth-child(1) > div.article__body.js-mediator-article.mia-analytics").text
            mli.append(text)
            l_6 += 1
            driver.back()
        except:
            driver.find_element(By.CSS_SELECTOR, f'#content > div > div.layout-rubric__main > div > div.list.list-tags > div:nth-child({i}) > div.list-item__content > a.list-item__title.color-font-hover-only').click()
            time.sleep(1)
            text = driver.find_element(By.CSS_SELECTOR, "#endless > div.endless__item.m-active > div > div > div > div.layout-article__over > div.layout-article__main > div > div:nth-child(1) > div.article__body.js-mediator-article.mia-analytics").text
            mli.append(text)
            l_6 += 1
            driver.back()

    










    
    llist = [6] * l_6 #+ [1] * l_1 + [2] * l_2 + [3] * l_3 + [4] * l_4 + [5] * l_5 + [7] * l_7 + [8] * l_8 + [6] * 100
    df['content'] = mli
    df['topic'] = llist

    
except Exception as ex:
    print("--------------------------------------no-----------------")

    print(ex.__class__.__name__)

finally:
    driver.close()
    driver.quit()


print('succes!!!!!!!!!!!!!!!!!!')
df.to_csv('news_6.csv', index= False, index_label= False)