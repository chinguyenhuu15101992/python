from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#link youtube: https://www.youtube.com/watch?v=hfnBswCe4QE
from selenium.webdriver.common.keys import Keys
##STEP 1: Login linkedin

#import username and password
credential = open('login_credential')
line=credential.readlines()
username=line[0]
passsword=line[1]
print("-Finish importing the login credentials")

driver = webdriver.Chrome()
url='https://www.linkedin.com/login'
driver.get(url)
sleep(2)
# how to use find_element link:https://www.faqcode4u.com/faq/490707/find-element-by-commands-are-deprecated-in-selenium

#key in username
email_field = driver.find_element(By.ID,'username')
driver.implicitly_wait(10)
email_field.send_keys(username)
print('-Finish keying in email')

#key in password
sleep(3)
pass_field = driver.find_element(By.NAME,'session_password')
# driver.implicitly_wait(10)
pass_field.send_keys(passsword)
print('-Finish keying in password')
sleep(2)
#click login button
login_field = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
login_field.click()
print('-Finish logging in')
sleep(2)


#xpath for JOBs: //*[@id="global-nav"]/div/nav/ul/li[3]/a

#xpat for search bar: //*[@id="jobs-search-box-keyword-id-ember123"]

#Step 2: Search for the profile we want to crawl
search_field = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]')
print(search_field)
print(type(search_field))
search_field.click()
print('- click ok ')
sleep(2)
#input the search query to the search bar
# search_query = input("please input profile you want to crawl")
search_field.click()
print('- click ok2 ')
search_field.send_keys("SOFTWARE")
#search enter
search_field.send_keys(Keys.RETURN)
print('-Finish searching ....')