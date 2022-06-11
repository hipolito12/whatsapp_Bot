
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
