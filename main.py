import time
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GetTimePassed import test_date_parser
import  os

def FindChats(chat):
    try:
        
        if chat.find_element(by.CLASS_NAME, "_1pJ9J").is_displayed():
            nro=chat.find_element(by.CLASS_NAME, "_1pJ9J").text
            return True
        else:
            return False

    except:
        print("Error al encontrar")


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
try:


    located = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((by.CLASS_NAME, "_26lC3"))
    )

    contact = driver.find_elements(by.CLASS_NAME, "_3OvU8")
    time.sleep(1)
    for i in range(15):
        contactname = contact[i].find_element(by.CLASS_NAME, "zoWT4").text

        print(contactname)
      

        if contactname == "Irina" :
            if FindChats(contact[i]) == True:

                reception_time = contact[i].find_element(by.CLASS_NAME, "_1i_wG").text
                print(reception_time)
                stringParts = reception_time.split(" ")
                print(stringParts)
                test_date_parser(stringParts[0])
                #print(timediff)
            break
except:
    print("Error")
