


from flask import Flask ,request ,render_template

import math


app=Flask(__name__)


@app.route("/dospuntos")
def puntos():
    return render_template("dospuntos.html")


@app.route("/resultado",methods=["POST"])
def resultado():
    n1=float(request.form.get("txtNum1"))
    n2=float(request.form.get("txtNum2"))
    n3=float(request.form.get("txtNum3"))
    n4=float(request.form.get("txtNum4"))
   
    res = float(math.sqrt(n1-n2)**2 + (n3-n4)**2)
    
    return render_template("resultado.html",res=res)

if __name__ =="__main__":
    app.run(debug=True,port=3000)

















