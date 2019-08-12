from flask import Flask, render_template, request, redirect
import os

app=Flask(__name__)
infos=[]
basedir = os.path.abspath(os.path.dirname(__file__))
fname = ""
status = {}

@app.route("/", methods=['GET', 'POST'])
def control():
    if request.method == "POST":
        img = request.files.get('photo')
        path = basedir+"\\static\\photo\\"
        fname = img.filename
        file_path = path+fname
        img.save(file_path)
        return render_template("ControlUI.html", imgName=fname, status=status)

    return render_template("ControlUI.html", imgName="", status=status)
    
@app.route("/infos", methods=['GET', 'POST'])
def info():
    if request.method == "POST":
        info = request.form["led"]
        infos.append(info)
        if request.form["switch"] == '0':
            status[request.form["value"]] = False
        else:
            status[request.form["value"]] = True
    return render_template("infos.html", infos=infos)


if __name__=="__main__":
    app.run(debug=True)