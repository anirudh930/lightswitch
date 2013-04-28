
#! /usr/bin/env python

'''
###################################################################################
# Created by : asquared
# Description : awesomeness isn't built, it is BORN.
# File Name : paytest.py
# Creation Date : 28-04-2013
# Last Modified Date : Sun Apr 28 00:55:41 2013
###################################################################################

Description format: 
Input: One line description of what comes as input to this file. 
Output: One line description of what goes out of this file.
Future: Points of what has to be done next. 
(Optional) Process: Include this section when we have some major algorithms and complex functions 
being implemented. Minor explanations can be included in the output section.  
 
Input: 

Output: 

Future: 

Process: 
Sample code from github, to test the paypal sdk. 

'''

import paypalrestsdk
import logging

logging.basicConfig(level=logging.INFO)

paypalrestsdk.configure(
  mode="sandbox", # sandbox or live
  client_id="AdmkuxBPBKz3mQP3V484X0G1sqljSXXFerTSUwE2f2DirSyBSmYNFc3L2thJ",
  client_secret="EMuJ1hDhizWIU5EH7AqK9SUFreBPHGcLzlQBNI0GE_jU8vNUSlD5mNuVcTfr")

payment = paypalrestsdk.Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "credit_card",
    "funding_instruments": [{
      "credit_card": {
        "type": "visa",
        "number": "4417119669820331",
        "expire_month": "11",
        "expire_year": "2018",
        "cvv2": "874",
        "first_name": "Joe",
        "last_name": "Shopper" }}]},
  "transactions": [{
    "item_list": {
      "items": [{
        "name": "item",
        "sku": "item",
        "price": "1.00",
        "currency": "USD",
        "quantity": 1 }]},
    "amount": {
      "total": "1.00",
      "currency": "USD" },
    "description": "This is the payment transaction description." }]})

if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)


