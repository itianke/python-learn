# !/usr/bin/python3

# 从selenium里面导入 webdriver
import time
from selenium import webdriver

# 指定chrom的驱动 执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# 最大化浏览器窗口
driver.maximize_window()

# get 方法 打开指定网址
driver.get('http://pam.lzyun.com/login')

driver.delete_all_cookies()

# 找到输入框 输入用户名&密码
time.sleep(2)
element_mail = driver.find_element_by_xpath("//input[contains(@placeholder, '请输入用户名/手机/邮箱')]")
element_mail.send_keys('智慧建设')

element_password = driver.find_element_by_xpath("//input[contains(@placeholder, '请输入密码')]")
element_password.send_keys('lz123456')

# 找到搜索按钮 模拟点击事件
element_search_button = driver.find_element_by_class_name('btn-login')
element_search_button.click()

# 去掉遮罩层
time.sleep(2)
element_guide = driver.find_element_by_xpath("//div[@class='guide-start-modal-footer']/button[1]")
element_guide.click()

# 进入领筑工程云
lzCloud = driver.find_element_by_xpath("//ul[@id='driverId-3']/li[3]")
lzCloud.click()

# 进入经营管理
time.sleep(2)
jingying_btn = driver.find_element_by_xpath("//span[contains(text(), '经营管理')]")
jingying_btn.click()

# 进入报备管理
time.sleep(2)
baobei_btn = driver.find_element_by_xpath("//span[contains(text(), '报备管理')]")
baobei_btn.click()

# 进入报备申请页面
time.sleep(2)
apply_btn = driver.find_element_by_xpath("//span[contains(text(), '报备项目申请')]")
apply_btn.click()








