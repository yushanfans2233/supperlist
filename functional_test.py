from selenium import webdriver

options = webdriver.ChromeOptions()

# 处理SSL证书错误问题
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# 忽略无用的日志
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

browser = webdriver.Chrome(executable_path=r"F:\app\chromedriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title
