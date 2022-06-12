import pywhatkit as wk
import datetime


def Sendmenssage(name):
    try:
        with open("ContactInfo.txt", 'r') as file:
            for line in file:
                if name in line:
                    line = line.rstrip()
                    number = line.split(":")
                    now = datetime.datetime.now()
                    wk.sendwhatmsg(number[1], "Hello", str(
                        now.hour), str(now.minute))
                    file.close()

                    break
    except:
        print("Error sending message")
        file.close()
    pass
