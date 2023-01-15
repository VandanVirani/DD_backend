from flask import Flask,jsonify,request
# from flask_cors import CORS
import requests
import re
import json
url = "https://api.razorpay.com/v1/payment_links"



app =Flask(__name__)

@app.route('/')
def f():
    return "hiiii"
# CORS(app)
@app.route('/api',methods=["GET"])

def returnf():
    price = int(request.args["price"])
    items = request.args["items"]
    place = request.args["place"]
    mobile_no= request.args["number"]
    # print("xxxxxxxxxx",price,items)
    payload = json.dumps({
    "amount": price*100,
    "currency": "INR",
    "accept_partial": False,
    "description": "{}".format(items),
     "customer": {
    "name":"{}  {}".format(place,items),
    "contact": "{}".format(mobile_no)
  },
    "notify": {
        "sms": True,
        "email": True
    },
    "reminder_enable": False,
    "callback_url": "https://example-callback-url.com/",
    "callback_method": "get"
    })
    headers = {

    'Authorization': 'Basic cnpwX3Rlc3RfTFpkR3hRTk90MmtFaTg6dUlRTFhPZ3M1NWF2NWFyZ1NvcWI2d0JL',
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # print("cccccccccc",response)
    a=re.search('"short_url":',response.text).span()[1]+1
    b=re.search(',"status":',response.text).span()[0]-1
    paymentLink = response.text[a:b].replace("\\",'')
    # print(r)

    return jsonify({'d':paymentLink})



    
    

if __name__=="__main__":
    app.run(host="0.0.0.0")
