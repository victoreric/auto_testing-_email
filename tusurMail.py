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

#password error
passwd=driver.find_element_by_id('password')
passwd.send_keys('Sengtau99')
# passwd.send_keys('12345')
#remember
driver.find_element_by_name('remember').click()
#press enter or login
passwd.send_keys(Keys.RETURN)
#time wait
time.sleep(1)

try :
    # compose message
    driver.find_element_by_css_selector('.text-center > .btn').click()

    time.sleep(1)
    #input recipient
    driver.find_element_by_id('inputTo').send_keys('victorerik@yandex.ru')
    time.sleep(1)

    #input subject
    driver.find_element_by_id('inputSubject').send_keys('автоматизированное тестирование')
    time.sleep(1)

    # message
    driver.find_element_by_css_selector('.note-editable').send_keys('Автоматизирование тестирование с Selenium и Python \n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas fermentum eu purus dictum semper. Donec aliquet nisi quis sapien pulvinar tempus. Sed nec ultricies nibh. Integer eu ante leo. Aenean eros urna, hendrerit vitae bibendum sed, mollis eget nibh. Nunc vitae sagittis urna. Vestibulum varius, justo a luctus luctus, nunc elit gravida sem, sit amet ullamcorper orci neque vitae quam. Cras luctus dapibus hendrerit. \n Nunc iaculis viverra venenatis. In hac habitasse platea dictumst. Nam rutrum neque ut sagittis commodo. Duis turpis quam, luctus in ipsum eget, scelerisque malesuada augue. Nunc scelerisque magna purus, in lobortis est cursus quis. Vivamus convallis sagittis massa. Vivamus eget felis eu orci suscipit imperdiet. Ut vitae hendrerit sapien. Morbi nec convallis erat. Nullam dignissim nisi erat, eu vehicula ligula pellentesque ac.\n Suspendisse potenti. Nullam gravida nulla quis ipsum tincidunt semper. Suspendisse potenti. Praesent neque felis, bibendum quis nibh sed, consequat blandit elit. Vestibulum scelerisque metus eget urna placerat, sit amet faucibus dolor elementum. Nunc vel libero luctus mauris feugiat dictum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam a erat ultricies, pulvinar nunc quis, tempus lacus. Aliquam nec tempus nibh. Curabitur maximus tempus efficitur. Integer nisl erat, tristique nec sagittis in, maximus non dolor. Proin lorem nibh, ultricies cursus suscipit sit amet, imperdiet a velit. Integer blandit magna mi, commodo sagittis lacus interdum ac. In porttitor ut lacus ac varius. Nullam sodales ac purus in pulvinar.')

    # time.sleep(3)

    #capture message
    # raw_filename="/Users/victoreric/selenium/images/message.png"
    # driver.save_screenshot(raw_filename)
    # time.sleep(2)

    #upload file
    driver.find_element_by_xpath('//*[@id="input-attachment"]').send_keys('/Users/victoreric/selenium/images/news.doc') 
    driver.find_element_by_xpath('//*[@id="input-attachment"]').send_keys('/Users/victoreric/selenium/images/tusur_small.png') 
    time.sleep(1)

    #send message
    driver.find_element_by_css_selector('.btn-xs:nth-child(1)').click()
    # time.sleep(2)

    #confirm send
    driver.find_element_by_css_selector('.bulk-send-confirm').click()
    time.sleep(1)

    #SendMail
    driver.find_element_by_xpath('//*[@id="mailbox-list-5e5718d856c6c504f59ecb13"]/a/span[3]').click()
    time.sleep(1)

    driver.close()
    driver.quit()

except :
    raw_filename="/Users/victoreric/selenium/images/error_passw.png"
    driver.save_screenshot(raw_filename)
   
    driver.close()
    driver.quit()




