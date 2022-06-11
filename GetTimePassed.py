from datetime import date
from datetime import datetime
from dateutil import parser
import datetime
def test_date_parser(time):



    try:


        a = datetime.datetime.strptime(time, '%H:%M')
        s = datetime.datetime.now().strftime("%H:%M")
        timeparse = datetime.datetime.strptime(s, '%H:%M') 
        print(timeparse)

       
    except ValueError as e:
        print("Error1", e)
