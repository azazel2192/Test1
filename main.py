from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_of_element_located(xpath):
    global dr
    element = WebDriverWait(dr, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


dr = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")  # указать путь к вебдрайверу

login = "dsy06067@xcoxc.com"
password = "123123Ee"
old_name = "Pozhiloy Ivan"
new_name = "Ivanov Ivan"

avatar_xpath = '//*[@id="topbar-menu"]/div/div[2]/div[4]/div[2]/a/avatar/div'
button_xpath = '/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[2]/div[5]' \
               '/button'
dr.get("https://app.clockify.me/en/login")

wait_of_element_located(button_xpath)
dr.find_element( By.XPATH, '//*[@id="email"]').send_keys(login)
dr.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
dr.find_element(By.XPATH, button_xpath).click()  # авторизация

wait_of_element_located(avatar_xpath)
dr.find_element(By.XPATH, avatar_xpath).click()
dr.find_element(By.XPATH, '//*[@id="topbar-menu"]/div/div[2]/div[4]/div[2]/div/a[1]').click()

name_element = dr.find_element(By.XPATH, '//*[@id="layout-main"]/div/userprofile/div/div/div[2]'
                                         '/div/div/div/div/div[2]/div[2]/div/div[1]/input')
name_element.clear()
name_element.send_keys(old_name)  # ставим первое имя, чтобы изменить его на второе
name_element.clear()
name_element.send_keys(new_name)  # ставим новое имя

toast_element = WebDriverWait(dr, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "toast-container")))
toast_element.click()
toast_text = toast_element.text

assert name_element.get_attribute("value") == new_name
assert "Settings successfully saved" in toast_text

dr.close()













