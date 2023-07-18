from selenium import webdriver
import pyautogui
import pyperclip

browser = webdriver.Chrome("C:/Users/sangmin/Desktop/git_practice/chromedriver.exe")
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
browser.implicitly_wait(10)

# id입력창

id = browser.find_element_by_xpath('//*[@id="id"]')
id.click()
# id.send_keys('bogus0115')
pyperclip.copy("bogus0115")
pyautogui.hotkey("ctrl","v")
pw = browser.find_element_by_xpath('//*[@id="pw"]')
pw.click()
# pw.send_keys('shtkd159!@')
pyperclip.copy("shtkd159!@")
pyautogui.hotkey("ctrl","v")
login = browser.find_element_by_xpath('//*[@id="log.login"]')
login.click()

nono = browser.find_element_by_xpath('//*[@id="new.dontsave"]')
nono.click()
