from flask import Flask,jsonify
app=Flask(__name__)
users=[{"id":100,
        "name":"Jayanta"},
        {"id":101,
         "name":"Umang"}
]
#Route to get all users
@app.route("/users",methods=["GET"])
def getUsers():
    return jsonify(users) 
if __name__=="__main__":
    app.run(debug=True)