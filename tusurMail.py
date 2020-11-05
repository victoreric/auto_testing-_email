from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time
driver=webdriver.Chrome()

#address
driver.get('https://e.tusur.ru/')
#max_window
driver.maximize_window()


#username
driver.find_element_by_id('username').send_keys('pattiraddzhavane.v.549-m@e.tusur.ru')

#password
passwd=driver.find_element_by_id('password')
passwd.send_keys('Sengtau99')
#remember
driver.find_element_by_name('remember').click()
#press enter or login
passwd.send_keys(Keys.RETURN)

time.sleep(5)

#capture home page
raw_filename="/Users/victoreric/selenium/images/emailtusur.png"
driver.save_screenshot(raw_filename)

#time wait
time.sleep(3)
# compose message
driver.find_element_by_css_selector('.text-center > .btn').click()

time.sleep(3)
#input recipient
driver.find_element_by_id('inputTo').send_keys('victorerik@yandex.ru; victoreric1409@gmail.com; chepurovova@yandex.ru')
time.sleep(3)

#input subject
driver.find_element_by_id('inputSubject').send_keys('автоматизированное тестирование. \n  Я не использую hotmail, потому что не могу найти способ получить загрузку файла элемента.\n Поэтому я решил воспользоваться почтовым сервисом TUSUR.\n  source code : https://github.com/victoreric/auto_testing_email \n \n  С уважением, \n  Виктор Э.П  ')
time.sleep(5)

# message
driver.find_element_by_css_selector('.note-editable').send_keys('Автоматизирование тестирование с Selenium и Python')
time.sleep(5)

#capture message
raw_filename="/Users/victoreric/selenium/images/message.png"
driver.save_screenshot(raw_filename)
time.sleep(5)

#upload file
driver.find_element_by_xpath('//*[@id="input-attachment"]').send_keys('/Users/victoreric/selenium/images/message.png') 

driver.find_element_by_xpath('//*[@id="input-attachment"]').send_keys('/Users/victoreric/selenium/images/emailtusur.png')
time.sleep(10)

#send message
driver.find_element_by_css_selector('.btn-xs:nth-child(1)').click()
time.sleep(3)

#confirm send
driver.find_element_by_css_selector('.bulk-send-confirm').click()
time.sleep(3)

#SendMail
driver.find_element_by_xpath('//*[@id="mailbox-list-5e5718d856c6c504f59ecb13"]/a/span[3]').click()
time.sleep(5)

driver.close()
driver.quit()




