from flask import Flask, request, jsonify, Response
import requests

server = Flask(__name__)

@server.route("/")
def welcome():
    return "Welcome !"
    
@server.route("/accounts", methods=['GET'])
def get_accounts():        
    name = request.args.get('name')
    if name:
        users = getUsers(name)
    else:
        users = getAllUsers()
    return jsonify(users)

@server.route("/users", methods=['GET'])
def get_users():
    apiKey = request.args.get('apiKey')
    if not apiKey:
        return "apiKey cannot be blank"
    elif "abcdef" != apiKey:
        return "invalid apiKey"
        
    name = request.args.get('name')
    if name:
        users = getUsers(name)
    else:
        users = getAllUsers()
    return jsonify(users)
    
@server.route("/users", methods=['POST'])
def create_user():
    apiKey = request.args.get('apiKey')
    if not apiKey:
        return "apiKey cannot be blank"
    elif "abcdef" != apiKey:
        return "invalid apiKey"
        
    return "Just wanted to let you know that, your request is rcvd." + str(request.json)
    
def getAllUsers():
    users = [
       {
          "id":1,
          "firstName":"Lance",
          "lastName":"Sterling",
          "profileName":"htuv",
          "email":"lance.sterling@invalid.com"
       },
       {
          "id":2,
          "firstName":"James",
          "lastName":"Bond",
          "profileName":"MI6",
          "email":"james.bond@invalid.com"
       },
       {
          "id":3,
          "firstName":"Ethan",
          "lastName":"Hunt",
          "profileName":"IMF",
          "email":"ethan.hunt@invalid.com"
       },
       {
          "id":4,
          "firstName":"Johnny",
          "lastName":"English",
          "profileName":"MI6",
          "email":"johnny.enghlish@invalid.com"
       },
       {
          "id":5,
          "firstName":"Zohan",
          "lastName":"Divir",
          "profileName":"MSD",
          "email":"zohan.divir@invalid.com"
       }
    ]
    return users
    
def getUsers(name):
  users = getAllUsers()
  result = []
  for user in users:
    if name.lower() in user['firstName'].lower() or name.lower() in user['lastName'].lower():
      result.append(user)
  return result
    

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=9090)
