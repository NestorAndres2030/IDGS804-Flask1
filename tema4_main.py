from flask import Flask
from flask import request

app = Flask(_name_)

@app.route("/suma", methods=["GET","POST"])
def suma():


    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        opt=request.form.get("opr")
        if opt == "SUMAR":
            res = float(num1) + float(num2)
        if opt == "RESTAR":
            res = float(num1) - float(num2)
        if opt == "MULTI":
            res = float(num1) * float(num2)
        if opt == "DIVISIO":
            res = float(num1) / float(num2)
        return "<h1> El numero es  {0} es: {1} </h1>".format(opt, res)
    else: 
        return '''
            <form action = '/suma' method="POST">
                <label>N1: </label>
                <input type="text" name="num1"/></br></br>
                
                <label>N2: </label>
                <input type="text" name="num2"/></br></br>
    
                <p>Selecciona la operación que deceas realiar:</p>
                <input type="radio" id="SUMA" name="opr" value="suma">
                <label for="suma">Suma</label><br>
                <input type="radio" id="RESTA" name="opr" value="resta">
                <label for="resta">Resta</label><br>  
                <input type="radio" id="age3" name="opr" value="100">
                <label for="MULTI">Multiplicacion</label><br>
                <input type="radio" id="DIVISION" name="opr" value="multiplicacion">
                <label for="division">Division</label><br><br>
                <input type="submit" value="Submit"> 
            </form>
        '''


if _name_ == "__main__": 
    app.run(
        debug = True,
        port = 3000
    )