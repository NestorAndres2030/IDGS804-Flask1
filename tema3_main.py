
from flask import Flask


app=Flask(__name__)


@app.route("/")
def index():
    return"Hola Mundo"

#pasamos un string

@app.route("/user/<string:user>")
def user(user):
    return"Hola " + user 

#pasamos parametro int

@app.route("/numero/<int:n>")
def user(n):
    return"Numero : {}".format(n) 
#Pasassr mas a de un parametro
@app.route("/username/<int:n>/<string:username>")
def usern(id,username):
    return"id:{} nombre:{}".format(id,username) 




if __name__ =="__main__":
    app.run(debug=True,port=3000)

