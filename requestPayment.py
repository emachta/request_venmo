# Author: Ennis Machta
# Description: Python script to handle venmo requests for donations from members of our lesson group

import client
import users
from venmo_api import Client
# docs: https://venmo.readthedocs.io/en/latest/

TRANSACTION_ID = "11"
DATE = "(01/31/2021)"  # Last sunday of each month


def requestPaymentFromUsersList(isReadyToChargeUsers):
    if isReadyToChargeUsers:
        inputResponse = input(
            "Are you sure you would like to charge the users? (type Y to continue) ")
        if inputResponse == "Y":
            for user in users.userList:
                personalMessage = "Orphan Sponsorship #{transactionId} {date} - {name}".format(
                    transactionId=TRANSACTION_ID, date=DATE, name=user["name"])
                client.venmo.payment.request_money(
                    20, personalMessage, user["id"])
            print("Request sent.")
    else:
        print("================== THIS IS A TEST ==================")
        for user in users.userList:
            personalMessage = "Orphan Sponsorship #{transactionId} {date} - {name}".format(
                transactionId=TRANSACTION_ID, date=DATE, name=user["name"])
            print(personalMessage)
        print("================== THIS IS A TEST ==================")