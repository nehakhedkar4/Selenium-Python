from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
# import pandas as pd
import csv
import random

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
driver.maximize_window()
driver.implicitly_wait(10)

# ------------------------LOGIN---------------------------
email = driver.find_element(By.XPATH,'//*[@id="username"]')
email.send_keys("nk.empiric@gmail.com")
time.sleep(3)
password = driver.find_element(By.XPATH,'//*[@id="password"]')
password.send_keys("neha0409!@")
password.send_keys(Keys.ENTER)
print("Logged in")
time.sleep(4)
# action = ActionChains(driver)

# # ------------Search-------------Python----------------------
# search = driver.find_element(By.XPATH,'//div[@class="search-typeahead-v2 search-global-typeahead__typeahead"]/input')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# print("Searched python")
# time.sleep(10)

# driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()
# print('CLicked to People')
# time.sleep(8)



# --------------Get data-------------
# profession = driver.find_element(By.XPATH,'//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "][2]/div[3]/ul/li/div/div[2]/div/div/div/span/span').text
# com = driver.find_element(By.XPATH,'//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "][2]/div[3]/ul/li[1]/div/div[2]/div/div[1]/span[1]/span').text
# timeD = driver.find_element(By.XPATH,'//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "][2]/div[3]/ul/li[1]/div/div[2]/div/div[1]/span[2]/span').text
# loc = driver.find_element(By.XPATH,'//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "][2]/div[3]/ul/li[1]/div/div[2]/div/div[1]/span[3]/span').text

# print(f"Neha Khedkar\n-----Experience:\n{profession}\n{com}.\n{timeD}\n{loc}.")
# time.sleep(10)


# index = 0
# ul = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div/ul')
# print("find ul")
# time.sleep(4)

# li = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div/ul/li')
# li = ul.find_elements(By.TAG_NAME,'li')
# # print(li.text)
# time.sleep(2)


# # -----------------------------------TO FIND USER'S EXPERIENCE------------------------------
# pro = driver.find_elements(By.XPATH,'//*[@class="reusable-search__result-container "]/div/div/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/a')
# path = '//*[@class="reusable-search__result-container "]/div/div/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/a'
# # print("pro")

# # print(len(pro))
# Info_lst = []
# c = 0
# while c < len(pro):
#     d = driver.find_elements(By.XPATH,'//*[@class="reusable-search__result-container "]/div/div/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/a')
#     d[c].click()
#     print("Clicked to profile")
#     time.sleep(10)

#     username = driver.find_element(By.XPATH,'//*[@class="artdeco-card ember-view pv-top-card"]/div[2]/div[2]/div/div/h1').text
#     print("found username, ",username)
#     # u_data = driver.find_element(By.XPATH,'//*[@class="artdeco-card ember-view relative break-words pb3 mt2 "][3]/div[3]/ul')
#     # print("found u_data")

#     # exp = driver.find_element(By.XPATH,'//*[@class="artdeco-card ember-view relative break-words pb3 mt2 "][3]/div[3]/ul/li[1]/div/div[2]/div/div[1]/div/span/span[1]').text
#     # print(exp)
#     # print(u_data.text)
    
#     exp = driver.find_element(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li[1]/div/div[2]/div/div[1]/div/span/span[1]').text
#     print("found exp",exp)
#     com = driver.find_element(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li[1]/div/div[2]/div/div[1]/span[1]/span[2]').text
#     print("found exp",com)
#     date = driver.find_element(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li[1]/div/div[2]/div/div[1]/span[2]/span[2]').text
#     print("found exp",date)
#     dic = {
#         'User' : username,
#         'Experience' : exp,
#         'Company' : com,
#         'From' : date,
#     }

#     Info_lst.append(dic)
#     df = pd.DataFrame(Info_lst)
#     c=c+1
#     print("c:",c)
#     driver.back()
#     time.sleep(7)

# df.to_csv('table.csv')
# print("saved to file")
# print(Info_lst)
# time.sleep(7)


# ------------------------SEND CONNECT REQUEST TO RANDOM USER--------------------------------
# connect_btn_list = []
# connect_btn = driver.find_elements(By.XPATH,'//ul[@class="reusable-search__entity-result-list list-style-none"]/li/div/div/div[3]/div/button')
# print('found connect button')
# time.sleep(8)
# i = 0
# while i < len(connect_btn):
#     c = driver.find_elements(By.XPATH,'//ul[@class="reusable-search__entity-result-list list-style-none"]/li/div/div/div[3]/div/button')
#     c[i].click()
#     print("clicked on connect")
#     time.sleep(4)
#     driver.find_element(By.XPATH,'//div[@id="artdeco-modal-outlet"]/div/div/div[3]/button[2]').click()
#     print("send")
#     print("i:",i)
#     i= i+1
#     time.sleep(3)

# print("done")

connect_btn_list = []
connect_btn = driver.find_elements(By.XPATH,'//ul[@class="reusable-search__entity-result-list list-style-none"]/li/div/div/div[3]/div/button')

for i in connect_btn:
    connect_btn_list.append(i)

random_connect_ch = random.choice([True,False])
print("random connection choice: ",random_connect_ch)

for c in connect_btn_list:
    if random_connect_ch:
        time.sleep(2)
        c.click()
        print("clicked on connect")
        time.sleep(4)
        driver.find_element(By.XPATH,'//div[@id="artdeco-modal-outlet"]/div/div/div[3]/button[2]').click()
        print("Invitation send!")
        time.sleep(5)
print("done")

# ----------------------------LIKE-------------------------------------------

# l = driver.find_elements(By.XPATH,"//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span/button[1]")

# # l = driver.find_element(By.XPATH,"//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span/button[1]")
# # # print("like button found")
# # # print(l.get_attribute('aria-pressed'))

# print("len: ",len(l))
# index = 0
# while index <len(l):
#     like_btn = driver.find_elements(By.XPATH,"//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span/button[1]")
#     comment_btn = driver.find_elements(By.XPATH,'//*[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[2]/span/div[1]/button')
#     print("found comment btn")
   
#     # # -------------------------------Like, if there is not liked---------
#     # check = like[index].get_attribute('aria-pressed')
#     # print("attr = ",check)
#     # if check == "true":
#     #     pass
#     # like[index].click()
#     # print("click to LIKE button")
#     # time.sleep(5)

#     # # print("I'm about to scroll")
#     # # if l:
#     # for i in range(5):
#     #     print("in for loop")
#     #     driver.execute_script("window.scrollTo(0, 100);")
#     #     time.sleep(5)

#     # # print("Done with scrolling")
    
    
#     # ----------------random like-----------------------------------------------------------
#     a = [True,False]
#     choose = random.choice(a)
#     print("choose: ",choose)
#     if choose:
#         print("In True")
#         time.sleep(4)
#         like_btn[index].click()
#         time.sleep(3)
#         print("Liked post")
#         # comment_btn[index].click()
#         comment_txt = driver.find_element(By.XPATH,'//*[@class="social-details-social-activity update-v2-social-activity"]/div[3]/div/div[2]/form/div/div/div[1]')
#         print("found comnt text")
#         time.sleep(3)

#         comment_txt.send_keys(".")
#         print("commented")
#         time.sleep(3)

#         comment_post = driver.find_element(By.XPATH,'//*[@class="social-details-social-activity update-v2-social-activity"]/div[3]/div/div[2]/form/div[2]/button')
#         print("found post btn")
#         time.sleep(3)
#         comment_post.click()
#         print("comment posted")
#         time.sleep(3)

#     pass

#     index+=1

# time.sleep(5)


# --------------------------------------------RANDOM LIKE & COMMENT --------------------------------------------------------------------------------
# SCROLL THE PAGE
# for scroll in range(2):
#     body = driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
#     time.sleep(4)

like_btn_list = []
comment_btn_list = []
like_btn = driver.find_elements(By.XPATH,"//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span/button[1]")
comment_btn = driver.find_elements(By.XPATH,"//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span[2]/span/div/button")
print(f'lenght of like_btn:{len(like_btn)} & comment:{len(comment_btn)}.')

for i in like_btn:
    like_btn_list.append(i)   
for j in comment_btn:  
    comment_btn_list.append(j)
# # print(like_btn_list)
# # print()
# # print()
# # print()
# # print()
# # print(comment_btn_list)



for i,j in zip(like_btn_list,comment_btn_list):
    random_like = [True,False]
    random_comment = [True,False]
    random_like_ch = random.choice(random_like)
    random_comment_ch = random.choice(random_comment)
    print(f"random like choice is: {random_like_ch} & comment choice: {random_comment_ch}.")

    if random_like_ch:          # LIKE IS TRUE
        print("atttr: ",i.get_attribute('aria-pressed'))
        time.sleep(2)
        if i.get_attribute('aria-pressed') == "false":
            i.click()
            print("liked a post")
            time.sleep(4)
    print("out of like")
    if random_comment_ch:       # COMMENT IS TRUE 
        j.click()  
        print("clicked to cmnt btn")
        time.sleep(5)
        
        comment_txt = driver.find_element(By.XPATH,'//*[@class="social-details-social-activity update-v2-social-activity"]/div[3]/div/div[2]/form/div/div/div[1]/div/div/div/div/div/p').send_keys(".")
        print("comment has been sent!")
        time.sleep(5)

        post_btn = driver.find_element(By.XPATH,'//*[@class="social-details-social-activity update-v2-social-activity"]/div[3]/div/div[2]/form/div[2]/button').click()
        print("clicked to post btn")
        time.sleep(5)


time.sleep(10)












# weather app 
# if contry chnge find deployement 















