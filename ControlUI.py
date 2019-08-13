from flask import Flask, render_template, request, redirect, url_for
import os

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
infos = []
global fname
fname = ''
status = {}

@app.route("/", methods=['GET', 'POST'])
def control():
    global fname
    return render_template("ControlUI.html", imgName=fname, status=status)
    
@app.route("/infos", methods=['GET', 'POST'])
def info():
    if request.method == "POST":
        info = request.form["led"]
        infos.append(info)
        if request.form["switch"] == '0':
            status[request.form["value"]] = False
        else:
            status[request.form["value"]] = True
    return redirect(url_for("control"))
    # return render_template("infos.html", infos=infos)

@app.route("/image", methods=['GET', 'POST'])
def image():
    if request.method == "POST":
        img = request.files.get('photo')
        global fname
        fname = img.filename
        if fname != '':
            path = os.path.join(basedir, "static", "photo", fname)
            img.save(path)
    return redirect(url_for("control"))

if __name__=="__main__":
    app.run(port=8080, debug=True)