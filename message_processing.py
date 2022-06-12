from SendMenssage import Sendmenssage


def menssages(ToanswerList):
    try:

        waitingContact = []
        if waitingContact.length == 0:
            pass
        else:
            for i in range(ToanswerList.length):

                if ToanswerList[i] not in waitingContact:
                    Sendmenssage(ToanswerList[i])
                    waitingContact.append(ToanswerList[i])
                break
    except Exception as e:
        print(e+'\n'+'Error in message_processing.py')
