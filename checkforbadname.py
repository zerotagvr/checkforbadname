import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

# Add more bad names if you want. 
# DO NOT REMOVE THIS if you do then people wont get banned for putting a bad name

listofbannablenames = [
    "NAZI", "ADOLFHITLER", "NAZ1", "FAG", "FAGGOT", "NIGGER", "NIGGA",
    "NIG", "SLAVE", "SLAVEOWNER", "PORN", "PORNOWNER", "PORNHUB",
    "XVIDEOS", "XVIDEOSOWNER", "CHILDPORN" #add more if you want
]

@app.route('/')
def home():
    return "The Url/Check for bad name is working"


# put your url then the /api/CheckForBadName 
# like this randomurl.vercel/api/CheckForBadName same for replit or pythonanywhere
@app.route('/api/CheckForBadName', methods=['POST', 'GET'])
def CheckForBadName():
    room = request.get_json().get("FunctionArgument", {}).get("forRoom")
    name = request.get_json().get("FunctionArgument", {}).get("name")

    if name in listofbannablenames:
        return jsonify({
            "result": 2
        }), 200
    
    else:
        return jsonify({
            "result": 0
        })