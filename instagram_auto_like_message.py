from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://instagram.com")
sleep(2)

#Login
driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
    .send_keys("username")  #username-Enter userame
driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
    .send_keys("password")   #password-Enter password
driver.find_element_by_xpath(("//button[@type=\"submit\"]"))\
    .click()
sleep(6)
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
    .click()
sleep(3)
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
    .click()
sleep(4)

#Like First Post
driver.find_element_by_class_name("_97aPb")
driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]/button")\
    .click()
driver.find_element_by_class_name("xWeGp").click()
sleep(5)

#Message People
hidden_element1 = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div")
if hidden_element1.is_enabled():
    driver.find_element_by_class_name("OEMU4").click()
    driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")\
        .send_keys("Hey!! Welcome to my account.")
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")\
        .click()
    sleep(4)
    hidden_element2 = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a/div/div[3]/div")
    if hidden_element2.is_enabled():
        driver.find_element_by_class_name("OEMU4").click()
        driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea") \
            .send_keys("Tata Khatam")
        sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button") \
            .click()
else:
    driver.close()





