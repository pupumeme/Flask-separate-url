from flask import Flask, render_template, request, redirect
import os

app=Flask(__name__)
infos=[]
basedir = os.path.abspath(os.path.dirname(__file__))
fname = ""

@app.route("/", methods=['GET', 'POST'])
def control():
    if request.method == "POST":
        img = request.files.get('photo')
        path = basedir+"\\static\\photo\\"
        fname = img.filename
        file_path = path+fname
        img.save(file_path)
        return render_template("ControlUI.html", imgName=fname)

    return render_template("ControlUI.html", imgName="")
    
@app.route("/infos", methods=['GET', 'POST'])
def info():
    if request.method == "POST":
        info = request.form["led"]
        infos.append(info)
    return render_template("infos.html", infos=infos)

@app.route('/up_photo', methods=['post'])
def up_photo():
    img = request.files.get('photo')
    path = basedir+"\\static\\photo\\"
    file_path = path+img.filename
    img.save(file_path)
    return "上傳成功" 

if __name__=="__main__":
    app.run(debug=True)