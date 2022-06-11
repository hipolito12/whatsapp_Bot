for i in range(15):
    contactname = contact[i].find_element_by_class_name("zoWT4").text
    if contactname == "Amor":
        contact[i].click()
        msg_box = driver.find_element_by_class_name("_1UWac _1LbR4")
        msg_box.send_keys("Hola", contactname,
                          "el creador de este bot se encuentra ocupado.")
        time.sleep(1)
        msg_box.send_keys(Keys.ENTER)
        msg_box.send_keys(
            "Hasta que se digne a contestar ,contemple las siguientes acciones : ")
        # aca van opciones
        time.sleep(1)
        msg_box.send_keys(Keys.ENTER)
        break

    break