from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/suma",methods=["GET","POST"])
def func():
    if request.methods=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return"<h1>la suma es :{}</h1>",format(str(int(num1)+int(num2)))

    else:
        return'''
        <form action="/suma" method="POST">
        <label>N1:</label>
        <input type="text" name="num1"><br><br><br>
        <label>N2:</label>
        <input type="text" name="num2"><br><br><br>
        <input type="sumit" value="calcular"><br><br><br>
        </form>
''' 

if __name__ =="__main__":
    app.run(debug=True,port=3000)