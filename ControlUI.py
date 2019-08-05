from flask import Flask, render_template, request, redirect
app=Flask(__name__)
infos=[]
@app.route("/", methods=['GET', 'POST'])
def control():
    return render_template("ControlUI.html")
    
@app.route("/infos", methods=['GET', 'POST'])
def info():
    if request.method == "POST":
        info = request.form["led"]
        infos.append(info)
    return render_template("infos.html", infos=infos)
if __name__=="__main__":
    app.run(debug=True)