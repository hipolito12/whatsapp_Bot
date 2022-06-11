
from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GetTimePassed import test_date_parser


def FindChats(chat):
    try:
        element = chat.find_element(
            by.CLASS_NAME, 'l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt')
        if element.is_displayed():
            return True
        else:
            return False

    except:
        print("Error al encontrar")


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
try:

    time.sleep(30)  

    contact = driver.find_elements(by.CLASS_NAME, "_3OvU8")
    time.sleep(1)
    for i in range(15):
        contactname = contact[i].find_element(by.CLASS_NAME, "zoWT4").text

        time.sleep(1)

        if contactname == "Amor" or contactname == "Amor💖":
            if FindChats(contact[i]) == True:

                reception_time = contact[i].find_element(by.CLASS_NAME, "_1i_wG").text
                print(reception_time)
                stringParts = reception_time.split(" ")
                print(stringParts)
                timediff= test_date_parser(stringParts[0])
                print(timediff)
            else:
                print("No hay mensajes")
                
                  
            

            break
        

except:
    print("Error")
